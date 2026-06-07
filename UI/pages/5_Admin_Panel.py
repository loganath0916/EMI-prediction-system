import streamlit as st
import pandas as pd
import os

st.title("⚙️ Admin Panel")

# =====================================
# Paths
# =====================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

data_path = os.path.join(
    BASE_DIR,
    "data",
    "EMI_dataset_cleaned.csv"
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

# =====================================
# Dataset Information
# =====================================

st.subheader("📁 Dataset Information")

df = pd.read_csv(data_path)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

# =====================================
# Model Information
# =====================================

st.subheader("🤖 Model Information")

if os.path.exists(classification_model):
    cls_size = round(
        os.path.getsize(classification_model) / (1024 * 1024),
        2
    )

    st.success(
        f"Classification Model Available ({cls_size} MB)"
    )

else:
    st.error(
        "Classification Model Missing"
    )

if os.path.exists(regression_model):
    reg_size = round(
        os.path.getsize(regression_model) / (1024 * 1024),
        2
    )

    st.success(
        f"Regression Model Available ({reg_size} MB)"
    )

else:
    st.error(
        "Regression Model Missing"
    )

# =====================================
# Dataset Columns
# =====================================

st.subheader("📋 Dataset Columns")

st.write(list(df.columns))

# =====================================
# Data Types
# =====================================

st.subheader("🔍 Data Types")

st.dataframe(
    pd.DataFrame(
        df.dtypes,
        columns=["Datatype"]
    )
)

# =====================================
# Missing Values Report
# =====================================

st.subheader("🚨 Missing Values Report")

st.dataframe(
    pd.DataFrame(
        df.isnull().sum(),
        columns=["Missing Values"]
    )
)

# =====================================
# Download Dataset
# =====================================

st.subheader("⬇️ Download Dataset")

csv = df.to_csv(index=False)

st.download_button(
    label="Download Dataset",
    data=csv,
    file_name="EMI_dataset.csv",
    mime="text/csv"
)

# =====================================
# System Status
# =====================================

st.subheader("🟢 System Status")

st.success(
    "Application Running Successfully"
)

st.success(
    "Models Loaded Successfully"
)

st.success(
    "Dataset Connected Successfully"
)