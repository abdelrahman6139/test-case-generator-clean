// ✅ backend/routes/fileUpload.js (FULL FILE)
const express = require('express');
const multer = require('multer');
const cors = require('cors');
const path = require('path');
const fs = require('fs');
const fetch = require('node-fetch');
const { extractTextFromPDF, extractTextFromDocx } = require('../utils/textExtractor');

const router = express.Router();
router.use(cors());

// File upload setup
const upload = multer({
  dest: 'uploads/',
  fileFilter: (req, file, cb) => {
    const allowedTypes = [
      'application/pdf',
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ];
    if (!allowedTypes.includes(file.mimetype)) {
      return cb(new Error('Only PDF and DOCX files are allowed'), false);
    }
    cb(null, true);
  }
});

// Upload endpoint
router.post('/upload', upload.single('file'), async (req, res) => {
  try {
    if (!req.file) return res.status(400).json({ message: 'No file uploaded' });

    let extractedText = '';
    if (req.file.mimetype === 'application/pdf') {
      extractedText = await extractTextFromPDF(req.file.path);
    } else if (req.file.mimetype === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document') {
      extractedText = await extractTextFromDocx(req.file.path);
    } else {
      return res.status(400).json({ message: 'Unsupported file format' });
    }

    const sentencesArray = extractedText
      .split('.')
      .map(s => s.trim())
      .filter(s => s.length > 0);

    const response = await fetch('http://127.0.0.1:5000/classify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sentences: sentencesArray })
    });

    if (!response.ok) {
      const errorText = await response.text();
      return res.status(500).json({ message: 'Error from Flask API', error: errorText });
    }

    const results = await response.json();
    const combinedResults = sentencesArray.map((sentence, index) => ({
      sentence,
      classification: results.results[index] || 'Unknown'
    }));

    const requirements = combinedResults.filter(item => item.classification === 'Requirement');
    const nonRequirements = combinedResults.filter(item => item.classification !== 'Requirement');

    const testCases = await generateTestCases(requirements);

    fs.unlink(req.file.path, err => {
      if (err) console.error('Failed to delete file:', err);
    });

    return res.json({ requirements, nonRequirements, testCases });
  } catch (error) {
    console.error('Error in /upload route:', error);
    return res.status(500).json({ message: 'Internal Server Error', error: error.message });
  }
});

const generateTestCases = async (requirements) => {
  try {
    const promises = requirements.map(async (requirement) => {
      try {
        const response = await fetch('http://127.0.0.1:5001/generate_test_case', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ requirement: requirement.sentence })
        });

        if (!response.ok) return 'Failed to generate test case.';

        const data = await response.json();
        return data.test_case || 'No test case generated.';
      } catch (err) {
        console.error('Error generating test case:', err);
        return 'Error occurred during test case generation.';
      }
    });

    return await Promise.all(promises);
  } catch (mainError) {
    console.error('Error in generateTestCases:', mainError);
    return requirements.map(() => 'General error.');
  }
};

module.exports = router;
