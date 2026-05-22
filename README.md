# 🏦 Loan Approval Prediction System

An intelligent Flask-based web application that predicts loan approval status using a trained Artificial Neural Network (ANN) built with TensorFlow/Keras. The system analyzes applicant financial details and provides instant loan approval predictions while securely storing application records in a SQLite database.

---

## 🚀 Features

✅ Loan approval prediction using Deep Learning (ANN)  
✅ Clean and responsive Flask web interface  
✅ SQLite database integration with SQLAlchemy ORM  
✅ Feature scaling using a pre-trained `StandardScaler`  
✅ Automatic storage of loan applications and prediction history  
✅ Real-time approval/rejection result generation  
✅ Structured ML preprocessing pipeline  
✅ Easy deployment and lightweight architecture  

---

## 🧠 Machine Learning Model

The prediction system uses:

- **Artificial Neural Network (ANN)**
- Built using **TensorFlow/Keras**
- Preprocessed with **StandardScaler**
- Binary classification output:
  - `APPROVED`
  - `REJECTED`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web framework |
| TensorFlow / Keras | Deep learning model |
| NumPy | Numerical operations |
| SQLite | Database |
| SQLAlchemy | ORM for database management |
| Pickle | Model scaler serialization |

---

## 📁 Project Structure

```bash
loan-approval-prediction/
│
├── app.py                     # Main Flask application
│
├── models/
│   ├── ann_model.h5           # Trained ANN model
│   └── scaler.pkl             # Saved StandardScaler
│
├── templates/
│   ├── index.html             # Home page
│   ├── loan.html              # Loan application form
│   └── output.html            # Prediction result page
│
├── static/                    # CSS, JS, images
│
├── loan_applications.db       # SQLite database
├── requirements.txt           # Project dependencies
└── README.md
