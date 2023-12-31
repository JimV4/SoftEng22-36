const express = require('express');
const morgan = require('morgan');
const dotenv = require('dotenv');
const bp = require('body-parser');
const cookieParser = require('cookie-parser');

const adminRouter = require(`${__dirname}/routes/adminRoutes.js`);
const authRouter = require(`${__dirname}/routes/authRoutes.js`);
const questionnaireRouter = require(`${__dirname}/routes/questionnaireRoutes.js`);
const questionRouter = require(`${__dirname}/routes/questionRoutes.js`);
const answerRouter = require(`${__dirname}/routes/answerRoutes.js`);
const sessionAnswerRouter = require(`${__dirname}/routes/sessionAnswerRoutes.js`);
const questionAnswerRouter = require(`${__dirname}/routes/questionAnswerRoutes.js`);
const sessionRouter = require(`${__dirname}/routes/sessionRoutes.js`);
const dummyDataRouter = require(`${__dirname}/routes/dummyDataRoutes.js`);

const app = express();

const host = process.env.HOST || 'localhost';

dotenv.config({ path: `${__dirname}/config.env` });

if (process.env.NODE_ENV === 'development') {
    app.use(morgan('dev'));
}

// Global middleware
app.use(bp.json());
app.use(bp.urlencoded({ extended: true }));
app.use(cookieParser());

// Authentication endpoints
app.use('/intelliq_api', authRouter);

// Admin endpoints
app.use('/intelliq_api/admin', adminRouter);

// Use case endpoints
app.use('/intelliq_api/questionnaire', questionnaireRouter); // a + additional
app.use('/intelliq_api/question', questionRouter); // b
app.use('/intelliq_api/doanswer', answerRouter); // c
app.use('/intelliq_api/getsessionanswers', sessionAnswerRouter); // d
app.use('/intelliq_api/getquestionanswers', questionAnswerRouter); // e

// Additional endpoints
app.use('/intelliq_api/session', sessionRouter);
app.use('/intelliq_api/dummy-data', dummyDataRouter);

// endpoints that don't exist on the api
app.all('*', (req, res) => {
    return res.status(400).json({
        status: 'failed',
        message: `Can't find ${req.originalUrl} on this server!`,
    });
});

module.exports = app;
