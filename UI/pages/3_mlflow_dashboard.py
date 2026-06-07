import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ==================================
# PAGE CONFIG
# ==================================
st.set_page_config(
    page_title="Model Monitoring Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Model Performance Dashboard")
st.markdown("---")

# ==================================
# MODEL FILE STATUS
# ==================================
st.subheader("📦 Saved Models")

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

classification_model = os.path.join(
    BASE_DIR,
    "Models",
    "best_classification_model.pkl"
)

regression_model = os.path.join(
    BASE_DIR,
    "Models",
    "best_regression_model.pkl"
)

if os.path.exists(classification_model):
    st.success("✅ Classification Model Available")
else:
    st.error("❌ Classification Model Missing")

if os.path.exists(regression_model):
    st.success("✅ Regression Model Available")
else:
    st.error("❌ Regression Model Missing")

st.markdown("---")

# ==================================
# CLASSIFICATION COMPARISON
# ==================================
st.subheader("🏆 Classification Model Comparison")

classification_df = pd.DataFrame({
    "Algorithm": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],
    "Accuracy": [
        0.84,
        0.86,
        0.87
    ],
    "Precision": [
        0.83,
        0.85,
        0.87
    ],
    "Recall": [
        0.82,
        0.84,
        0.86
    ]
})

st.dataframe(
    classification_df,
    use_container_width=True
)

fig1 = px.bar(
    classification_df,
    x="Algorithm",
    y="Accuracy",
    color="Algorithm",
    title="Classification Accuracy Comparison"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown("---")

# ==================================
# REGRESSION COMPARISON
# ==================================
st.subheader("📈 Regression Model Comparison")

regression_df = pd.DataFrame({
    "Algorithm": [
        "Linear Regression",
        "Random Forest",
        "XGBoost"
    ],
    "R2 Score": [
        0.567,
        0.599,
        0.601
    ],
    "RMSE": [
        5113,
        4921,
        4909
    ],
    "MAE": [
        3728,
        3547,
        3537
    ]
})

st.dataframe(
    regression_df,
    use_container_width=True
)

fig2 = px.bar(
    regression_df,
    x="Algorithm",
    y="R2 Score",
    color="Algorithm",
    title="Regression R² Score Comparison"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

fig3 = px.bar(
    regression_df,
    x="Algorithm",
    y="RMSE",
    color="Algorithm",
    title="RMSE Comparison (Lower is Better)"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# ==================================
# SELECTED MODELS
# ==================================
st.subheader("🥇 Selected Models")

st.success("""
Best Classification Model: XGBoost

Accuracy: 87%

Selected for EMI Eligibility Prediction
""")

st.success("""
Best Regression Model: XGBoost

R² Score: 0.601

RMSE: 4909

Selected for EMI Amount Prediction
""")

st.markdown("---")

# ==================================
# DEPLOYMENT STATUS
# ==================================
st.subheader("🚀 Deployment Status")

deployment_df = pd.DataFrame({
    "Component": [
        "Classification Model",
        "Regression Model",
        "Streamlit Application"
    ],
    "Status": [
        "Running",
        "Running",
        "Active"
    ]
})

st.dataframe(
    deployment_df,
    use_container_width=True
)

st.markdown("---")
st.caption("EMI Prediction System - Model Monitoring Dashboard")