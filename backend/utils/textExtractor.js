const fs = require('fs');
const pdf = require('pdf-parse');
const mammoth = require('mammoth');

// Function to extract text from a PDF file
async function extractTextFromPDF(filePath) {
    try {
        const dataBuffer = fs.readFileSync(filePath);
        const data = await pdf(dataBuffer);
        return data.text;
    } catch (error) {
        console.error("Error extracting text from PDF:", error);
        throw error;
    }
}

// Function to extract text from a DOCX file
async function extractTextFromDocx(filePath) {
    try {
        const data = await mammoth.extractRawText({ path: filePath });
        return data.value;
    } catch (error) {
        console.error("Error extracting text from DOCX:", error);
        throw error;
    }
}

// Export the functions so they can be used in other files
module.exports = { extractTextFromPDF, extractTextFromDocx };
