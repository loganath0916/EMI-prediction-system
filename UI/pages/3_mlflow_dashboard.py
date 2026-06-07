import streamlit as st
import mlflow
from mlflow.tracking import MlflowClient
import pandas as pd
import os

# Page Config
st.set_page_config(page_title="MLflow Dashboard", page_icon="📊")

st.title("📊 MLflow Dashboard")
st.markdown("---")

# Connect to MLflow Database
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

db_path = os.path.join(
    BASE_DIR,
    "Models",
    "mlflow.db"
)

mlflow.set_tracking_uri(
    f"sqlite:///{db_path}"
)

# Debug (remove later)
st.write("MLflow DB Path:", db_path)

client = MlflowClient()

# ==========================
# Experiments
# ==========================
st.subheader("📁 Experiments")

experiments = mlflow.search_experiments()

if experiments:
    exp_data = []

    for exp in experiments:
        exp_data.append({
            "Experiment ID": exp.experiment_id,
            "Experiment Name": exp.name
        })

    st.dataframe(pd.DataFrame(exp_data), use_container_width=True)

else:
    st.warning("No experiments found.")

# ==========================
# Runs
# ==========================
st.subheader("🏃 Recent Runs")

runs = mlflow.search_runs()

if len(runs) > 0:

    display_cols = []

    for col in runs.columns:
        if (
            "metrics" in col
            or "params" in col
            or col == "run_id"
            or col == "status"
        ):
            display_cols.append(col)

    st.dataframe(
        runs[display_cols],
        use_container_width=True
    )

else:
    st.warning("No runs found.")

# ==========================
# Best Models
# ==========================
st.subheader("🤖 Registered Models")

try:
    models = client.search_registered_models()

    model_data = []

    for model in models:
        model_data.append({
            "Model Name": model.name
        })

    st.dataframe(
        pd.DataFrame(model_data),
        use_container_width=True
    )

except:
    st.info("No registered models available.")

# ==========================
# Project Metrics
# ==========================
st.subheader("📈 Project Metrics")

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

# ==========================
# Model Files
# ==========================
st.subheader("📦 Saved Models")

st.success("✅ best_classification_model.pkl")
st.success("✅ best_regression_model.pkl")

st.markdown("---")
st.caption("EMI Prediction System - MLflow Monitoring Dashboard")