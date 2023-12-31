const mongoose = require('mongoose');
const slugify = require('slugify');
const validator = require('validator');

const questionSchema = new mongoose.Schema({
    qID: {
        type: String,
        required: [true, 'A question must have an id'],
        unique: [true, "A question must have it's own unique id"],
        maxlength: [3, 'A question id must have 3 characters'],
        minlength: [3, 'A question id must have 3 characters'],
    },
    qtext: {
        type: String,
        required: [true, 'A question cannot be blank'],
    },
    required: {
        type: String,
        enum: {
            values: ['TRUE', 'FALSE'],
            message: 'Required is TRUE or FALSE',
        },
        required: [true, 'You must answer this question!'],
    },
    type: {
        type: String,
        enum: {
            values: ['question', 'profile'],
            message: 'Required is question or profile',
        },
        required: [true, 'A question must have a type']
    },
    options: [
        {
            type: mongoose.Schema.ObjectId,
            ref: 'Option',
        },
    ],
    wasAnsweredBy: {
        type: Number,
        default: 0,
    },
    questionnaireID: {
        type: String,
    },
});

const Question = mongoose.model('Question', questionSchema);

module.exports = Question;
