const Questionnaire = require(`${__dirname}/../models/questionnaireModel.js`);
const Question = require(`${__dirname}/../models/questionModel.js`);
const Option = require(`${__dirname}/../models/optionModel.js`);
const Session = require(`${__dirname}/../models/sessionModel.js`);
const Answer = require(`${__dirname}/../models/answerModel.js`);
const User = require(`${__dirname}/../models/userModel.js`);
const mongoose = require('mongoose');
const converter = require('json-2-csv');
const csv = require('csv-express');

const handleResponse = (req, res, statusCode, responseMessage) => {
    if (req.query.format === 'json' || !req.query.format) {
        return res.status(statusCode).json(...responseMessage);
    } else if (req.query.format === 'csv') {
        return res.status(statusCode).csv(responseMessage, true, {}, statusCode);
    } else {
        return res.status(400).json({
            status: 'failed',
            message: 'Response format must be either json or csv!',
        });
    }
};

/**
 * Creates and stores an answer object in the database.
 * @param {JSON} req - JSON request object containing questionnaireID, questionID, sessionID and optionID (req.params), answer text (req.body).
 * @param {JSON} res - JSON response object containing a confirmation/rejection of the request.
 * @return {JSON} - The response object.
 * 
 * URL: {baseURL}/doanswer/:questionnaireID/:questionID/:session/:optionID
*/
exports.doAnswer = async (req, res, next) => {
    let session, option, question, questionnaire,
        newAnswer = {
            qID: req.params.questionID,
            optID: req.params.optionID,
            sessionID: req.params.session,
            questionnaireID: req.params.questionnaireID,
            answertext: req.body.answertext ? req.body.answertext : ''
        },
        newAnswerCreated = false, optionUpdated = false, questionUpdated = false;
    try {
        /* 1) CHECK VALIDITY OF PARAMETERS GIVEN */
        /* If user is not allowed to answer, reject the request */
        let user = await User
            .findOne({ username: req.username, role: 'user' }, '_id role questionnairesAnswered')
            .populate('questionnairesAnswered', 'questionnaireID');

        /* If questionnaireID or questionID or optionID is unvalid, reject the request */
        questionnaire = await Questionnaire
            .findOne({ questionnaireID: req.params.questionnaireID }, '_id questionnaireID questions')
            .populate({
                path: 'questions',
                model: 'Question',
                match: { qID: req.params.questionID },
                select: '_id qID options wasAnsweredBy',
                populate: {
                    path: 'options',
                    model: 'Option',
                    match: { optID: req.params.optionID },
                    select: '_id optID wasChosenBy nextqID opttxt',
                }
            });

        let inputValid = true;
        const questionnaireValid = questionnaire;
        if (questionnaireValid) {
            question = questionnaire.questions[0];
            const questionValid = questionnaire.questions.length;
            if (questionValid) {
                option = question.options[0];
                const optionValid = question.options.length;
                inputValid = optionValid;
            } else inputValid = false;
        } else inputValid = false;
        if (!inputValid) {
            return handleResponse(req, res, 400, [{
                status: 'failed',
                message: 'Arguments provided are invalid'
            }]);
        }



        /* 2) CHECK IF A SESSION ALREADY EXISTS */
        session = await Session
            .findOne({ sessionID: req.params.session }, '-questionnaireID -__v')
            .populate('answers', '_id qID optID answertext');

        if (session) {
            /* Search session.answers[] for an answer._id  */
            const answersArrayEmpty = (session.answers.length === 0);
            if (!answersArrayEmpty) {
                let answerIndex = session.answers.findIndex(ans => ans.qID === req.params.questionID);
                if (answerIndex > -1) {
                    session.answers.forEach(async ans => {
                        let ques = await Question.findOne({ qID: ans.qID }, 'wasAnsweredBy');
                        ques.wasAnsweredBy -= 1;
                        ques = await ques.save();

                        let opt = await Option.findOne({ optID: ans.optID }, 'wasChosenBy');
                        opt.wasChosenBy -= 1;
                        opt = await opt.save();

                        await Answer.findByIdAndDelete(ans._id);
                    });

                    await Answer.deleteMany({ sessionID: req.params.session });
                    await Session.findOneAndRemove({ sessionID: req.params.session });

                    const responseMessage = [{
                        status: 'failed',
                        message: 'An answer has already been submitted for this question',
                        'previous answer': (
                            session.answers[answerIndex].answertext !== '' ?
                                session.answers[answerIndex].answertext :
                                (await Option.findOne({ optID: session.answers[answerIndex].optID })).opttxt
                        )
                    }];
                    return handleResponse(req, res, 400, responseMessage);
                }
            }
        } else {
            session = await Session.create({
                sessionID: req.params.session,
                questionnaireID: req.params.questionnaireID,
                answers: [],
                submitter: req.username
            });
        }



        /* 3) SUBMIT NEW ANSWER TO DB */
        newAnswer = await Answer.create(newAnswer);
        newAnswerCreated = true;
        session.answers.push(newAnswer._id);
        session = await session.save();



        /* 4) UPDATE FIELDS IN RELEVANT DOCUMENTS (questions & options) */
        option.wasChosenBy += 1;
        option = await option.save();
        optionUpdated = true;
        question.wasAnsweredBy += 1;
        question = await question.save();
        questionUpdated = true;

        if (option.nextqID === '-') {
            const alreadyAnswered = user['questionnairesAnswered'].some(q => q['_id'].toString() === questionnaire._id.toString());
            if (!alreadyAnswered) {
                await user.updateOne({ $push: { questionnairesAnswered: questionnaire._id } });
            }
        }


        /* 5) SEND RESPONSE */
        return handleResponse(req, res, 200, [{
            status: 'OK',
            message: 'Answer submitted!'
        }]);
    } catch (error) {
        console.log(error);
        await Session.findByIdAndDelete(session['_id']);
        if (newAnswerCreated) {
            await Answer.findByIdAndDelete(newAnswer._id);

            if (optionUpdated) {
                option.wasChosenBy = option.wasChosenBy - 1;
                await option.save();

                if (questionUpdated) {
                    --(question.wasAnsweredBy);
                    await question.save();
                }
            }
        }

        return handleResponse(req, res, 500, [{
            status: 'failed',
            message: error.name + error.message
        }]);
    }
    next();
};

/**
 * Returns all the answers of a specified session.
 * @param {JSON} req - JSON object containing questionnaireID and sessionID (req.params).
 * @param {JSON} res - JSON object containing the data to send.
 * @return {JSON} - The response object.
 * 
 * URL: {baseURL}/getsessionanswers/:questionnaireID/:session
 */
exports.getSessionAnswers = async (req, res, next) => {
    /* This line is added only for temporary purposes */
    return res.status('418').json({ status: 'no operation', message: 'I\'m a teapot' });
};

/**
 * Returns all the answers of a specified question.
 * @param {JSON} req - JSON object containing qustionnaireID and questionID (req.params).
 * @param {JSON} res - JSON object containing the data to send.
 * @return {JSON} - The response object.
 * 
 * URL: {baseURL}/getquestionanswers/:questionnaireID/:questionID
 */
exports.getQuestionAnswers = async (req, res, next) => {
    /* This line is added only for temporary purposes */
    return res.status('418').json({ status: 'no operation', message: 'I\'m a teapot' });
};
