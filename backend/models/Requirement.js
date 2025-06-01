const mongoose = require('mongoose');

const RequirementSchema = new mongoose.Schema({
    sentence: { type: String, required: true },
    classification: { type: String, required: true },
    createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Requirement', RequirementSchema);
