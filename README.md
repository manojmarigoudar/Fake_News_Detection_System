# Fake News Detection System

A Machine Learning and Natural Language Processing (NLP) based web application that detects whether a news article is **Real** or **Fake**.

---

# 📌 Project Overview

The Fake News Detection System analyzes news text entered by the user and predicts whether the news is:

* ✅ Real News
* ❌ Fake News

This project uses:

* Machine Learning
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Logistic Regression
* Streamlit Web Application

---

# 🚀 Features

* Detects fake news automatically
* Simple and user-friendly interface
* Real-time prediction
* Uses NLP techniques for text analysis
* Fast and lightweight ML model

---

# 🛠 Technologies Used

| Technology          | Purpose                  |
| ------------------- | ------------------------ |
| Python              | Programming Language     |
| Streamlit           | Frontend Web Application |
| Pandas              | Data Handling            |
| NumPy               | Numerical Operations     |
| Scikit-learn        | Machine Learning         |
| NLP                 | Text Processing          |
| TF-IDF              | Text Vectorization       |
| Logistic Regression | Classification Algorithm |

---

# 📂 Project Structure

```text
Fake_News_Detection_System/
│
├── news_app.py
├── news_model.py
├── fake_news_dataset.csv
├── fake_news_model.pkl
├── vectorizer.pkl
└── README.md
```

---

# 📊 Dataset Information

Dataset contains:

| Column | Description   |
| ------ | ------------- |
| title  | News headline |
| text   | News content  |
| label  | Output class  |

### Labels

| Value | Meaning   |
| ----- | --------- |
| 1     | Real News |
| 0     | Fake News |

---

# ⚙️ Machine Learning Workflow

```text
Dataset
   ↓
Text Cleaning
   ↓
TF-IDF Vectorization
   ↓
Model Training
   ↓
Prediction
```

---

# 🧠 Algorithm Used

## Logistic Regression

Logistic Regression is used for binary classification.

In this project:

* Real News = 1
* Fake News = 0

The model predicts whether the news entered by the user is real or fake.

---

# 🔍 What is TF-IDF?

TF-IDF stands for:

```text
Term Frequency – Inverse Document Frequency
```

It converts text data into numerical vectors so Machine Learning models can process text efficiently.

---

# 💻 Frontend

Frontend is developed using:

```text
Streamlit
```

Frontend Features:

* Text input area
* Check News button
* Prediction display
* Interactive web interface

---

# ⚡ Backend

Backend handles:

* Dataset loading
* Text processing
* TF-IDF vectorization
* Model training
* Prediction generation
* Saving trained model

---

# ▶️ How to Run the Project

## Step 1: Install Required Libraries

```bash
pip install pandas numpy scikit-learn streamlit nltk
```

---

## Step 2: Train the Model

Run:

```bash
python news_model.py
```

This creates:

* fake_news_model.pkl
* vectorizer.pkl

---

## Step 3: Run the Streamlit App

```bash
streamlit run news_app.py
```

---

# 🧪 Sample Test Inputs

## Real News Example

```text
Government launched a new education policy for students
```

## Fake News Example

```text
Aliens landed in India yesterday night
```

---

# 📈 Advantages

* Fast prediction
* Automatic fake news detection
* Easy to use
* Lightweight application
* Useful for media verification

---

# ⚠️ Limitations

* Small dataset
* Lower accuracy with limited data
* Cannot easily detect satire news
* Requires better datasets for higher accuracy

---

# 🔮 Future Enhancements

* Use larger datasets
* Add Deep Learning models (LSTM/BERT)
* Real-time news API integration
* Multi-language support
* Better UI design
* Improved model accuracy

---

# 📚 Conclusion

The Fake News Detection System successfully uses Machine Learning and NLP techniques to classify news articles as Real or Fake.

This project demonstrates the practical implementation of:

* Machine Learning
* Natural Language Processing
* Streamlit Web Applications

for solving misinformation problems.

---

# 👨‍💻 Author

**Manoj B M**

* Mini Project Developer
* Machine Learning & NLP Enthusiast
* Developed using Python, Streamlit, and Scikit-learn

