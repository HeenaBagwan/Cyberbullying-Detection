import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import os
import joblib

# Step 1: Download NLTK stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Step 2: Define text cleaning function
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters & numbers
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    return text.lower()  # Convert to lowercase

# Step 3: Load preprocessed dataset
print("Loading dataset...")
data = pd.read_csv('data/processed/preprocessed_data.csv')

# Step 4: Preprocess the text if not already done
if 'cleaned_text' not in data.columns:
    print("Cleaning text data...")
    data['cleaned_text'] = data['Text'].apply(clean_text)

# Use 'oh_label' as the label column
X = data['cleaned_text']
y = data['oh_label']

# Step 5: Split the dataset
print("Splitting dataset into training, validation, and test sets...")
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Step 6: Vectorize text using TF-IDF
print("Vectorizing text data with TF-IDF...")
vectorizer = TfidfVectorizer(max_features=5000)  # Use top 5000 words
X_train_tfidf = vectorizer.fit_transform(X_train)
X_val_tfidf = vectorizer.transform(X_val)
X_test_tfidf = vectorizer.transform(X_test)

# Step 7: Train the model
print("Training Logistic Regression model...")
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Step 8: Validate the model
print("Validating model...")
y_val_pred = model.predict(X_val_tfidf)
print("Validation Accuracy:", accuracy_score(y_val, y_val_pred))
print("Classification Report on Validation Set:\n", classification_report(y_val, y_val_pred))

# Step 9: Test the model
print("Testing model...")
y_test_pred = model.predict(X_test_tfidf)
print("Test Accuracy:", accuracy_score(y_test, y_test_pred))
print("Classification Report on Test Set:\n", classification_report(y_test, y_test_pred))

# After training the model and before saving it, add this:
output_dir = 'ML/model/'
os.makedirs(output_dir, exist_ok=True)

# Now save the model
joblib.dump(model, os.path.join(output_dir, 'logistic_regression_model.pkl'))

# Step 10: Save the model and vectorizer
print("Saving model and vectorizer...")
joblib.dump(model, 'ML/model/logistic_regression_model.pkl')
joblib.dump(vectorizer, 'ML/model/tfidf_vectorizer.pkl')
print("Model and vectorizer saved successfully.")
