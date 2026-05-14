import joblib
from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)
model = joblib.load('model/fraud_model.pkl')

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Analyze Transaction
@app.route('/analyze', methods=['POST'])
def analyze():

    upi_id = request.form['upi']
    amount = int(request.form['amount'])
    message = request.form['message'].lower()
    risk_score = 0
    prediction = model.predict([message])[0]

    # ML Scam Detection
    if prediction == 1:
       risk_score += 40
    suspicious_words = [
        "urgent",
        "click now",
        "verify",
        "lottery",
        "reward",
        "otp",
        "bank blocked",
        "free",
        "win money"
    ]

    # Check suspicious words
    for word in suspicious_words:
        if word in message:
            risk_score += 20
    
    # Financial transaction behavior analysis

    financial_words = [
         "payment",
         "transfer",
         "balance",
         "refund",
         "pending",
         "account"
    ]

    for word in financial_words:

        if word in message and amount > 30000:
            risk_score += 25
            
    # Check suspicious URLs
    suspicious_urls = [
        "bit.ly",
        "tinyurl",
        ".ru",
        ".tk"
    ]

    for url in suspicious_urls:
        if url in message:
            risk_score += 25

    # High amount check
    if amount > 50000:
        risk_score += 30

    # Limit score to 100
    if risk_score > 100:
        risk_score = 100

    # Final Risk Status
    if risk_score >= 70:
        status = "HIGH RISK"

    elif risk_score >= 40:
        status = "SUSPICIOUS"

    else:
        status = "SAFE"

    return render_template(
        'result.html',
        upi=upi_id,
        amount=amount,
        message=message,
        score=risk_score,
        status=status,
        prediction=prediction
    )


import os

if __name__ == '__main__':

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host='0.0.0.0',
        port=port
    )