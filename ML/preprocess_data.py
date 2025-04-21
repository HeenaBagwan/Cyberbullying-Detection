import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

# Download NLTK stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Define text cleaning function
def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters & numbers
    text = re.sub(r"\s+", " ", text)  # Remove extra spaces
    return text.lower()  # Convert to lowercase

# Load dataset
data = pd.read_csv('data/raw/cyberbullying_dataset.csv')

# Inspect dataset columns
print("Dataset Columns:", data.columns)

# Clean the text
data['cleaned_text'] = data['Text'].apply(clean_text)

# Use 'oh_label' as the label column
X = data['cleaned_text']
y = data['oh_label']

# Display sample data
print("Sample cleaned data:")
print(data[['cleaned_text', 'oh_label']].head())

# Save preprocessed data
data.to_csv('data/processed/preprocessed_data.csv', index=False)
print("Preprocessed data saved to 'data/processed/preprocessed_data.csv'.")
