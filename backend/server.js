const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const bodyParser = require('body-parser');
const connectDB = require('./config/db');


// Load environment variables
dotenv.config();

// Connect to MongoDB
connectDB();

const app = express();

// Middleware
app.use(cors()); 
app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: true }));

// Test route
app.get('/', (req, res) => {
  res.send('API is running...');
});

// Import routes
const authRoutes = require('./routes/auth');
const fileUploadRoutes = require('./routes/fileUpload');
const requirementRoutes = require('./routes/requirementRoutes'); // ✅ Requirement CRUD Routes
const katalonRoutes = require('./routes/katalonRoutes');

app.use('/api', authRoutes); 
app.use('/api', fileUploadRoutes);
app.use('/api/requirements', requirementRoutes); 
app.use('/api', katalonRoutes);
// ✅ Ensure Requirement CRUD Works

// Start server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`✅ Server running on port ${PORT}`);
});
