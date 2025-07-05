# dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Load predictions
df = pd.read_csv("predictions.csv")

# Title
st.title("📊 Loan Default Prediction Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

default_filter = st.sidebar.selectbox(
    "Prediction", options=["All", "Default (1)", "No Default (0)"]
)

if default_filter == "Default (1)":
    df = df[df["prediction"] == 1]
elif default_filter == "No Default (0)":
    df = df[df["prediction"] == 0]

threshold = st.sidebar.slider(
    "Minimum Probability of Default", min_value=0.0, max_value=1.0, value=0.5
)
df = df[df["probability_of_default"] >= threshold]

# Main stats
st.write(f"### Showing {len(df)} predictions")

# Histogram of probability scores
fig = px.histogram(
    df,
    x="probability_of_default",
    nbins=20,
    title="Distribution of Default Probability",
)
st.plotly_chart(fig)

# Table
st.dataframe(df.head(50))
