import sys
import joblib
import pandas as pd
import re

# Load the model and vectorizer once at the start
model = joblib.load('ML/model/logistic_regression_model.pkl')
vectorizer = joblib.load('ML/model/tfidf_vectorizer.pkl')

# Clean the input text
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters & numbers
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    return text.lower()  # Convert to lowercase

# Get input text from the command line argument
input_text = sys.argv[1]

# Preprocess the input text
cleaned_text = clean_text(input_text)

# Vectorize the cleaned text
input_vector = vectorizer.transform([cleaned_text])

# Predict the label (0 for neutral, 1 for bullying)
prediction = model.predict(input_vector)

# Map prediction to human-readable labels
prediction_label = "bullying" if prediction[0] == 1 else "neutral"

# Output the prediction
print(prediction_label)
