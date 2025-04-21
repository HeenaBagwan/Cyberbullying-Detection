const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const { predict } = require('./predict');

const app = express();
const PORT = 5000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Define the /predict route
app.post('/predict', async (req, res) => {
  const { text } = req.body;

  if (!text) {
    return res.status(400).json({ error: 'No text provided' });
  }

  try {
    const prediction = await predict(text); 
    res.json({ prediction });
  } catch (error) {
    console.error('Error:', error.message);
    res.status(500).json({ error: 'Failed to get prediction' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Node.js server running on http://localhost:${PORT}`);
});
