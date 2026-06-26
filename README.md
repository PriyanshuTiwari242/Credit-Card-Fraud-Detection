# 💳 Credit Card Fraud Detection Web Application

A full-stack Machine Learning web application that detects fraudulent credit card transactions using a trained Logistic Regression model. The application provides secure user authentication, real-time fraud prediction, CSV batch analysis, prediction history, and an interactive dashboard through a modern Flask-based web interface.

---

## 📌 Features

- 🔐 User Registration & Login
- 🔒 Password Hashing using Flask-Bcrypt
- 👤 Session Management
- 🤖 Real-Time Credit Card Fraud Prediction
- 📂 CSV Batch Prediction
- 📊 Dashboard with Prediction Statistics
- 📜 Prediction History Tracking
- 💾 SQLite Database Integration
- 🌐 Responsive User Interface
- ⚡ REST API built with Flask

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- SQLite

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Frontend
- HTML5
- CSS3
- JavaScript

### Authentication
- Flask-Bcrypt
- Flask Sessions

### Development Tools
- Jupyter Notebook
- VS Code

---

## 📂 Project Structure

```
creditcard_fraud_detection/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── users.db
├── creditcard.csv
├── requirements.txt
├── README.md
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
│
└── static/
    ├── css/
    ├── js/
    └── images/
```

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
```

### 2️⃣ Navigate to the Project

```bash
cd credit-card-fraud-detection
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📸 Application Modules

- 🏠 Home Page
- 👤 User Signup
- 🔑 User Login
- 📊 Dashboard
- 💳 Fraud Prediction
- 📂 CSV Upload
- 📜 Prediction History
- 🚪 Logout

---

## 🤖 Machine Learning Workflow

1. Load Credit Card Dataset
2. Data Preprocessing
3. Feature Scaling
4. Train Logistic Regression Model
5. Save Model using Pickle
6. Load Model in Flask
7. Predict Fraudulent Transactions
8. Display Results to Users

---

## 🔐 Authentication Features

- Secure Password Hashing
- User Registration
- User Login
- Session Management
- Logout Functionality

---

## 📊 Dashboard

The dashboard displays:

- Total Predictions
- Fraudulent Transactions
- Safe Transactions
- Prediction History

---

## 🎯 Future Enhancements

- 📈 Interactive Charts (Chart.js)
- ☁️ Cloud Deployment (Render)
- 🐘 PostgreSQL Database
- 📧 Email Notifications
- 📱 Mobile Responsive UI
- 👨‍💼 Admin Dashboard
- 🔍 Prediction Search & Filters
- 📥 Export Prediction History

---

## 👨‍💻 Author

**Priyanshu Tiwari**

B.Tech Computer Science & Engineering

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
