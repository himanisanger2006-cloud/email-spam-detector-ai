# 📧 Spam Email Classifier (CSV Based)

A Machine Learning project that classifies emails as **Spam 🚫** or **Not Spam ✅** using NLP techniques and models like Logistic Regression and Naive Bayes.

---

## 📌 Features

- CSV-based dataset support (Kaggle format compatible)  
- Text preprocessing (cleaning, normalization)  
- TF-IDF vectorization with n-grams  
- Multiple ML models:  
  - Logistic Regression  
  - Naive Bayes  
- Hybrid rule-based spam detection  
- Real-time user input prediction  
- Model saving and loading using pickle  

---

## 🛠️ Tech Stack

- Python  
- Pandas & NumPy  
- Scikit-learn  
- Regex & String Processing  
- Pickle (Model Serialization)  

---

## 📂 Project Structure

```
spam-email-classifier/
│
├── spam.csv              # Dataset file
├── main.py               # Main Python script
├── vectorizer.pkl        # Saved TF-IDF vectorizer
├── spam_model.pkl        # Saved trained model
└── README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

Follow these steps to run the project on your system:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/spam-email-classifier.git
cd spam-email-classifier
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install pandas numpy scikit-learn
```

---

### 4️⃣ Add Dataset

- Place your dataset file named **spam.csv** in the project folder.  
- Dataset should contain:  
  - `v1` → label (ham/spam)  
  - `v2` → text message  

---

## ▶️ How to Run the Project

Run the Python script:

```bash
python main.py
```

---

## 💻 Usage

Once the program starts:

- Enter an email/message in the terminal  
- Get prediction instantly  

**Example:**

```
Enter email (or 'exit'): Congratulations! You won a free lottery
📊 Prediction: SPAM 🚫
```

To stop:

```
exit
```

---

## 🧠 Model Details

### 🔹 Text Processing
- Lowercasing  
- Removing URLs, numbers, punctuation  

### 🔹 Vectorization
- TF-IDF  
- Max features: 5000  
- N-grams: (1,3)  

### 🔹 Models Used
- Logistic Regression (primary)  
- Multinomial Naive Bayes  

### 🔹 Smart Detection

Includes keyword-based spam boosting:

```
urgent, verify, compromised, click, winner, free, lottery, prize
```

---

## 📊 Evaluation Metrics

- Accuracy Score  
- Confusion Matrix  
- Classification Report  

---

## 💾 Model Saving

After training, the model is saved as:

```
vectorizer.pkl
spam_model.pkl
```

---

## 🔄 Load Saved Model (Optional)

```python
vec, model = load_model()
```

---

## 🚀 Future Improvements

- Add GUI (Tkinter / Streamlit)  
- Use Deep Learning (LSTM / BERT)  
- Deploy as Web App  
- Improve dataset size & accuracy  

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a new branch  
3. Make changes  
4. Submit a pull request  

---

## 📜 License

This project is for educational purposes.
