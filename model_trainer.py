import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import joblib
import os

print("Starting Model Training...")

# Load the data from news.csv
try:
    df = pd.read_csv('news.csv')
    X = df['text']  # The news article text
    y = df['label']  # The 0 or 1 label (Real/Fake)
except Exception as e:
    print(f"Error loading news.csv: {e}")
    exit()

# Split data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 1. Create the Vectorizer (The Translator: turns words into numbers)
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train = tfidf_vectorizer.fit_transform(X_train.fillna(''))

# 2. Create and Train the Model (The Learner)
pac_model = PassiveAggressiveClassifier(max_iter=50)
pac_model.fit(tfidf_train, y_train)

# 3. Save the Brains! (The model and the vectorizer)
joblib.dump(pac_model, 'pac_model.joblib')
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.joblib')

print("SUCCESS: Model and Vectorizer saved! Ready to connect to Django.")
