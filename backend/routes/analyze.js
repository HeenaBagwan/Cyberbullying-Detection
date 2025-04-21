const express = require('express');
const router = express.Router();
const analyzeText = require('../utils/mlModel');

// POST endpoint for text analysis
router.post('/', (req, res) => {
  const { text } = req.body;

  if (!text) {
    return res.status(400).json({ error: 'Text input is required' });
  }

  try {
    // Call the ML model for prediction
    const result = analyzeText(text);

    // Return the result
    res.json({ result });
  } catch (error) {
    console.error('Error analyzing text:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

module.exports = router;
