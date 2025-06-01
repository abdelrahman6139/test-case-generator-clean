const express = require('express');
const Requirement = require('../models/Requirement');

const router = express.Router();

// ✅ Create (Save Requirements)
router.post('/save', async (req, res) => {
    try {
        const { sentence, classification } = req.body;

        if (!sentence || !classification) {
            return res.status(400).json({ message: 'Sentence and classification are required' });
        }

        const newRequirement = new Requirement({ sentence, classification });
        await newRequirement.save();
        res.status(201).json(newRequirement);
    } catch (error) {
        res.status(500).json({ message: 'Error saving requirement', error: error.message });
    }
});

// ✅ Read (Get All Requirements)
router.get('/get', async (req, res) => {
    try {
        const requirements = await Requirement.find();
        res.json(requirements);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching requirements', error: error.message });
    }
});

// ✅ Update (Edit a Requirement)
router.put('/update/:id', async (req, res) => {
    try {
        const { sentence, classification } = req.body;

        const updatedRequirement = await Requirement.findByIdAndUpdate(
            req.params.id,
            { sentence, classification },
            { new: true }
        );

        if (!updatedRequirement) {
            return res.status(404).json({ message: 'Requirement not found' });
        }

        res.json(updatedRequirement);
    } catch (error) {
        res.status(500).json({ message: 'Error updating requirement', error: error.message });
    }
});

// ✅ Delete (Remove a Requirement)
router.delete('/delete/:id', async (req, res) => {
    try {
        const deletedRequirement = await Requirement.findByIdAndDelete(req.params.id);

        if (!deletedRequirement) {
            return res.status(404).json({ message: 'Requirement not found' });
        }

        res.json({ message: 'Requirement deleted successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Error deleting requirement', error: error.message });
    }
});

module.exports = router;
