import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="ML Dashboard", page_icon="📊")

st.title("📊 Model Performance Dashboard")
st.markdown("---")

# Model Files Status
st.subheader("📦 Saved Models")

base_dir = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

classification_model = os.path.join(
    base_dir,
    "Models",
    "best_classification_model.pkl"
)

regression_model = os.path.join(
    base_dir,
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

# Performance Metrics
st.subheader("📈 Model Metrics")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Classification Accuracy",
        value="87%"
    )

with col2:
    st.metric(
        label="Regression R² Score",
        value="0.60"
    )

st.markdown("---")

# Deployment Status
st.subheader("🚀 Deployment Status")

status_df = pd.DataFrame({
    "Component": [
        "Classification Model",
        "Regression Model",
        "Streamlit App"
    ],
    "Status": [
        "Running",
        "Running",
        "Active"
    ]
})

st.dataframe(
    status_df,
    use_container_width=True
)

st.markdown("---")
st.caption("EMI Prediction System Dashboard")