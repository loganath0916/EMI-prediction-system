# EMI Prediction System

## Overview

The EMI Prediction System is a Machine Learning-based financial analytics application that helps users evaluate loan eligibility and estimate the maximum EMI amount they can afford based on their financial profile.

The project combines Classification and Regression Machine Learning models and provides an interactive Streamlit web application for real-time predictions.

---

## Problem Statement

Financial institutions need to assess whether an applicant is eligible for a loan and determine an appropriate EMI amount based on income, expenses, credit history, and employment details.

This project automates the process using Machine Learning techniques.

---

## Features

### EMI Eligibility Prediction (Classification)

Predicts whether a customer is:

* Eligible
* Moderately Eligible
* Not Eligible

Algorithms Evaluated:

* Logistic Regression
* Random Forest Classifier
* XGBoost Classifier

Best Model:

* XGBoost Classifier

---

### EMI Amount Prediction (Regression)

Predicts the maximum affordable EMI amount for an applicant.

Algorithms Evaluated:

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

Best Model:

* XGBoost Regressor

---

## Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Joblib
* MLflow
* Streamlit

### Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub
* Streamlit Cloud

---

## Project Workflow

### Data Processing

* Data Cleaning
* Missing Value Handling
* Feature Engineering
* Feature Selection

### Machine Learning

Classification Pipeline:

* Train-Test Split
* Feature Scaling
* Model Training
* Model Evaluation
* MLflow Experiment Tracking

Regression Pipeline:

* Train-Test Split
* Model Training
* Performance Evaluation
* MLflow Experiment Tracking

---

## Model Evaluation

### Classification Metrics

* Accuracy
* Precision
* Recall
* F1 Score

### Regression Metrics

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

---

## MLflow Integration

MLflow was used for:

* Experiment Tracking
* Metric Logging
* Parameter Logging
* Model Comparison
* Best Model Selection

---

## Streamlit Application

The application consists of:

### Classification Page

Predicts EMI Eligibility using customer financial information.

### Regression Page

Predicts Maximum EMI Amount using customer financial information.

---

## Project Structure

```text
EMI-prediction-system/
│
├── data/
├── data_processed/
├── Models/
│   ├── best_classification_model.pkl
│   ├── best_regression_model.pkl
│
├── UI/
│   ├── app.py
│   └── pages/
│       ├── 1_Classification.py
│       └── 2_Regression.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Future Enhancements

* Loan Interest Rate Prediction
* Explainable AI (SHAP)
* Database Integration
* User Authentication
* Cloud-Based Model Monitoring
* API Deployment using FastAPI

---

## Author

Loganath C

Data Science & Machine Learning Enthusiast

GitHub:
https://github.com/loganath0916
