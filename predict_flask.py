from flask import Flask, request, jsonify
from flask import send_from_directory
from flask_cors import CORS
import joblib
import pandas as pd
import re
import time
import numpy as np

app = Flask(__name__, static_folder='public', static_url_path='')

CORS(app)


@app.route('/')
def home():
    return send_from_directory('public', 'index.html')


# Improved text preprocessing
def clean_text(text):
    text = re.sub(r'http\S+', '', text)  
    text = re.sub(r'[^a-zA-Z0-9.,!?\s]', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()  
    return text.lower()

# Load model once at startup
model = joblib.load('ML/model/logistic_regression_model.pkl')
vectorizer = joblib.load('ML/model/tfidf_vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get('text', '')

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Clean the input text before vectorizing
        cleaned_text = clean_text(text)

        # Transform the cleaned text to feature vector
        input_vector = vectorizer.transform([cleaned_text])

        # Get the model prediction probabilities
        prediction_proba = model.predict_proba(input_vector)[0]
        
        # Get the probability for bullying class (assuming class 1 is "bullying")
        bullying_prob = prediction_proba[1]

        # Lower threshold for bullying detection (adjust as needed)
        label = "Bullying" if bullying_prob >= 0.50 else "Neutral"

        return jsonify({"prediction": label})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
