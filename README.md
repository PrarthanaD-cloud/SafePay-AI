#  SafePay AI
### AI-Powered Fraud Guardian for First-Time Digital Users

SafePay AI is an intelligent fraud detection web application designed to protect first-time digital payment users from phishing attacks, scam messages, and suspicious transactions.

The system combines **Machine Learning**, **Natural Language Processing (NLP)**, and **rule-based cybersecurity techniques** to analyze risky transactions in real time and warn users before payment.

---

#  Live Demo

🔗 https://safepay-ai-ehzl.onrender.com

---

#  Problem Statement

With the rapid growth of digital payments and online banking, first-time digital users are increasingly vulnerable to:

- Phishing messages
- Scam payment requests
- Fraudulent links
- Fake reward scams
- Social engineering attacks

Most existing systems detect fraud **after** the transaction occurs.

SafePay AI focuses on:
## Preventing fraud BEFORE payment.

---

# Features

## AI/ML Scam Detection
- Detects phishing and scam messages using Machine Learning
- Uses NLP techniques for text classification

## Risk Scoring Engine
- Generates transaction risk score dynamically
- Classifies transactions as:
  - SAFE
  - SUSPICIOUS
  - HIGH RISK

## Multilingual Fraud Alerts
Supports:
- English
- Kannada
- Hindi

## Voice Warning System
- Provides spoken fraud warnings using browser speech synthesis
- Improves accessibility for elderly and beginner users

## Rule-Based Fraud Analysis
Detects:
- Suspicious keywords
- Phishing URLs
- High-risk payment amounts
- Scam patterns

## Professional UI
- Responsive dark-themed interface
- Dynamic risk indicators
- Progress/risk meter

---

# Machine Learning Model

The application uses:

- **TF-IDF Vectorization**
- **Logistic Regression**
- **SMS Spam Collection Dataset**

The model is trained to classify messages as:
- Scam
- Safe

---

# System Architecture

```text
User Input
   ↓
Flask Backend
   ↓
Rule-Based Fraud Analysis
   ↓
Machine Learning NLP Model
   ↓
Risk Score Calculation
   ↓
Voice + Multilingual Alerts
   ↓
Final Risk Classification
```

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Python
- Flask

## AI / Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression

## Dataset
- SMS Spam Collection Dataset

## Deployment
- Render

## Version Control
- Git
- GitHub

---

# Project Structure

```text
SafePay-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── model/
│   ├── train_model.py
│   └── fraud_model.pkl
│
└── dataset/
```

---

# Installation & Setup

## 1.Clone Repository

```bash
git clone https://github.com/PrarthanaD-cloud/SafePay-AI.git
```

---

## 2.Navigate to Project Folder

```bash
cd SafePay-AI
```

---

## 3.Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4.Run Application

```bash
python app.py
```

---

## 5.Open in Browser

```text
http://127.0.0.1:5000
```

---

# Sample Test Cases

## Scam Example

```text
Congratulations! You won ₹50,000. Click now to claim reward.
```

Expected Output:
- HIGH RISK
- Scam Detected
- Voice Warning

---

## Safe Example

```text
Dinner payment to friend
```

Expected Output:
- SAFE
- Safe Message

---

# Security Features

- Phishing keyword detection
- Suspicious URL analysis
- Large transaction detection
- NLP-based scam prediction
- Voice-based warning alerts
- Multilingual safety notifications

---

# Future Enhancements

- QR code fraud detection
- Real-time banking API integration
- Mobile application support
- Advanced Deep Learning models
- Real-time threat intelligence
- User transaction history analytics
- AI chatbot assistant

---

# Project Goal

To improve digital trust and financial safety by helping first-time digital users identify fraudulent transactions before making payments.

---

# Developed By

**Prarthana D**  
Computer Science Engineering Student

---

# Acknowledgements

- Flask Documentation
- Scikit-learn Documentation
- SMS Spam Collection Dataset
- Render Deployment Platform

---

# License

This project is developed for educational and hackathon purposes.