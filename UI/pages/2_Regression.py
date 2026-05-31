import streamlit as st
import joblib
import pandas as pd
import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

model_path = os.path.join(
    BASE_DIR,
    "Models",
    "best_regression_model.pkl"
)

# DEBUG
st.write("Current Directory:", os.getcwd())
st.write("Model Path:", model_path)

reg_model = joblib.load(model_path)

# Title
st.title("💰 EMI Amount Prediction")

# Inputs
age = st.number_input(
    "Age",
    min_value=18,
    max_value=70,
    value=30
)

monthly_salary = st.number_input(
    "Monthly Salary",
    min_value=10000,
    value=30000
)

years_of_employment = st.number_input(
    "Years Of Employment",
    min_value=0.0,
    value=2.0
)

credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=700
)

bank_balance = st.number_input(
    "Bank Balance",
    min_value=0,
    value=100000
)

current_emi_amount = st.number_input(
    "Current EMI Amount",
    min_value=0,
    value=0
)

requested_amount = st.number_input(
    "Requested Amount",
    min_value=1000,
    value=500000
)

requested_tenure = st.number_input(
    "Requested Tenure (Months)",
    min_value=6,
    value=60
)

# Prediction
if st.button("Predict EMI Amount"):

    input_data = pd.DataFrame(
        [[
            age,
            monthly_salary,
            years_of_employment,
            credit_score,
            bank_balance,
            current_emi_amount,
            requested_amount,
            requested_tenure
        ]],
        columns=[
            "age",
            "monthly_salary",
            "years_of_employment",
            "credit_score",
            "bank_balance",
            "current_emi_amount",
            "requested_amount",
            "requested_tenure"
        ]
    )

    prediction = reg_model.predict(input_data)

    st.success(
        f"💰 Predicted EMI Amount: ₹{prediction[0]:,.2f}"
    )