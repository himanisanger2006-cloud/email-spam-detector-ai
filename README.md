# 📧 Spam Email Classifier (CSV Based)

A Machine Learning project that classifies emails as **Spam 🚫** or **Not Spam ✅** using NLP techniques and models like Logistic Regression and Naive Bayes.

---

## 📖 Introduction

With the rapid growth of digital communication, email has become one of the most widely used platforms for personal and professional interaction. However, this growth has also led to an increase in spam emails, which include unwanted advertisements, phishing attempts, and potentially harmful content. Detecting and filtering such emails is essential to ensure user safety and maintain productivity.

This project focuses on building a Spam Email Classifier using Machine Learning and Natural Language Processing (NLP) techniques. The system analyzes the content of emails and classifies them as either spam or not spam based on learned patterns from a dataset.

By using techniques like text preprocessing, TF-IDF vectorization, and classification models such as Logistic Regression and Naive Bayes, this project demonstrates an efficient and practical approach to spam detection. Additionally, a hybrid rule-based mechanism is incorporated to enhance prediction accuracy by identifying commonly used spam keywords.

Overall, this project serves as a beginner-friendly yet powerful implementation of text classification and provides a strong foundation for understanding real-world applications of machine learning in cybersecurity and communication systems.

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
---

## 📌 Conclusion

This project demonstrates how Machine Learning and Natural Language Processing can be effectively used to detect spam emails. By applying text preprocessing, TF-IDF vectorization, and classification algorithms like Logistic Regression and Naive Bayes, the system is able to accurately distinguish between spam and legitimate messages.

The addition of a hybrid rule-based approach further improves prediction reliability by capturing common spam patterns that models may sometimes miss. This makes the system more robust and practical for real-world usage.

Overall, this project provides a strong foundation in text classification, model building, and deployment concepts. It also highlights the importance of combining statistical models with domain knowledge to achieve better results. With further improvements such as larger datasets, deep learning models, and deployment as a web application, this system can be extended into a fully functional spam detection tool.

## 📜 License

This project is for educational purposes.
