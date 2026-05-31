import streamlit as st

st.set_page_config(
    page_title="EMI Prediction System",
    page_icon="💰",
    layout="wide"
)

st.title("💰 EMI Prediction System")

st.write("""
Welcome to the EMI Prediction System.

Use the sidebar to navigate between:
- EMI Eligibility Prediction
- EMI Amount Prediction
""")