const axios = require('axios');

// Function to call the Flask API and get predictions
const predict = async (userInput) => {
  const startTime = Date.now(); // Log start time
  try {
    const response = await axios.post('http://localhost:5000/predict', {
      text: userInput,
    });
    const endTime = Date.now(); // Log end time
    console.log(`Prediction time: ${(endTime - startTime) / 1000} seconds`);
    return response.data.prediction;
  } catch (error) {
    console.error('Error:', error.message);
    throw new Error('Error in prediction.');
  }
};

module.exports = { predict };
