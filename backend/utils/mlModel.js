// Mock ML Model Integration
function analyzeText(text) {
    // Placeholder logic: Identify "bullying" words (you can replace this with your ML model later)
    const bullyingKeywords = ['hate', 'stupid', 'ugly', 'idiot', 'worthless'];
    const containsBullying = bullyingKeywords.some((word) => text.toLowerCase().includes(word));
  
    return containsBullying ? 'Bullying' : 'Neutral';
  }
  
  module.exports = analyzeText;
  
