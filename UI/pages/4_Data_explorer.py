import streamlit as st
import pandas as pd
import os

st.title("📊 Data Explorer")

# Dataset Path
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

# Load Data
df = pd.read_csv(data_path)

# ===================================
# Dataset Overview
# ===================================

st.subheader("Dataset Overview")

st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

st.dataframe(df.head())

# ===================================
# Column Selector
# ===================================

st.subheader("Column Analysis")

selected_column = st.selectbox(
    "Choose a Column",
    df.columns
)

st.write(df[selected_column].describe())

# ===================================
# Missing Values
# ===================================

st.subheader("Missing Values")

missing = df.isnull().sum()

st.dataframe(
    missing[missing > 0]
)

# ===================================
# Correlation Matrix
# ===================================

st.subheader("Correlation Matrix")

numeric_df = df.select_dtypes(
    include=["int64", "float64"]
)

corr = numeric_df.corr()

st.dataframe(corr)

# ===================================
# Visualization
# ===================================

st.subheader("Visualization")

chart_column = st.selectbox(
    "Select Numeric Column",
    numeric_df.columns
)

st.bar_chart(
    numeric_df[chart_column]
)

# ===================================
# Download Dataset
# ===================================

st.subheader("Download Dataset")

csv = df.to_csv(index=False)

st.download_button(
    "Download CSV",
    csv,
    "EMI_dataset.csv",
    "text/csv"
)