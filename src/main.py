
# SPAM EMAIL CLASSIFIER (CSV BASED)


# Import Libraries
import pandas as pd
import numpy as np
import string
import re
import pickle

# Sklearn Libraries
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# STEP 1: LOAD DATASET FROM CSV


try:
    data = pd.read_csv("spam.csv", encoding='latin-1')

    # Handle Kaggle dataset format
    if 'v1' in data.columns and 'v2' in data.columns:
        data = data.rename(columns={'v1': 'label', 'v2': 'text'})

    data = data[['label', 'text']]

    print("✅ Dataset Loaded Successfully!")

except Exception as e:
    print("❌ Error loading dataset:", e)
    exit()

print("\nDataset Preview:")
print(data.head())

# STEP 2: DATA PREPROCESSING


# Convert labels
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Remove null values
data.dropna(inplace=True)

# Text Cleaning Function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)     # remove URLs
    text = re.sub(r'\d+', '', text)         # remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

# Apply cleaning
data['clean_text'] = data['text'].apply(clean_text)


# STEP 3: TRAIN-TEST SPLIT


X = data['clean_text']
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# STEP 4: TF-IDF VECTORIZATION (IMPROVED)

vectorizer = TfidfVectorizer(
    stop_words='english',
    max_features=5000,
    ngram_range=(1,3)   #  IMPORTANT FIX
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("\n✅ Vectorization Completed")


# STEP 5: MODEL TRAINING


lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_vec, y_train)

nb_model = MultinomialNB()
nb_model.fit(X_train_vec, y_train)

print("\n✅ Models Trained Successfully")


# STEP 6: MODEL EVALUATION


lr_pred = lr_model.predict(X_test_vec)
nb_pred = nb_model.predict(X_test_vec)

print("\n===== Logistic Regression =====")
print("Accuracy:", accuracy_score(y_test, lr_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, lr_pred))
print("Report:\n", classification_report(y_test, lr_pred))

print("\n===== Naive Bayes =====")
print("Accuracy:", accuracy_score(y_test, nb_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, nb_pred))
print("Report:\n", classification_report(y_test, nb_pred))


# STEP 7: SMART PREDICTION FUNCTION


def predict_email(text):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])

    lr_result = lr_model.predict(vectorized)[0]

    #  Hybrid Rule-Based Boost
    spam_keywords = [
        "urgent", "verify", "compromised",
        "click", "account", "winner",
        "free", "lottery", "prize"
    ]

    if any(word in cleaned for word in spam_keywords):
        final_result = 1
    else:
        final_result = lr_result

    print("\n📩 Input Email:", text)
    print("📊 Prediction:", "SPAM 🚫" if final_result == 1 else "NOT SPAM ✅")


# STEP 8: USER INPUT LOOP


while True:
    user_input = input("\nEnter email (or 'exit'): ")

    if user_input.lower() == 'exit':
        print("👋 Exiting program...")
        break

    predict_email(user_input)


# STEP 9: SAVE MODEL


with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("spam_model.pkl", "wb") as f:
    pickle.dump(lr_model, f)

print("\n✅ Model saved successfully!")


# STEP 10: LOAD MODEL (OPTIONAL)


def load_model():
    with open("vectorizer.pkl", "rb") as f:
        vec = pickle.load(f)

    with open("spam_model.pkl", "rb") as f:
        model = pickle.load(f)

    return vec, model


