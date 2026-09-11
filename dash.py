import streamlit as st
import pandas as pd

st.set_page_config(page_title="Filtered Sales Dashboard", layout="wide")
st.title("💰📊 AI Sales Dashboard")

# Load data
try:
    df = pd.read_csv("data/ai_dash_data.csv")
    st.success("✅ Data loaded successfully")

    # Region filter
    st.sidebar.header("Region Options")
    region = st.sidebar.selectbox("Choose Region", df['region'].unique())

    # Filter data
    filtered_df = df[df['region'] == region]

    # Show filtered table
    st.subheader(f"Region Data: {region}")
    st.dataframe(filtered_df)
    
    # Product filter
    st.sidebar.header("Product Options")
    product = st.sidebar.selectbox("Choose Product", df['product'].unique())

    # Filter data
    filtered_df = df[df['product'] == product]

    # Show filtered table
    st.subheader(f"Product Data: {product}")
    st.dataframe(filtered_df)
    
    # Status filter
    st.sidebar.header("Status Options")
    status = st.sidebar.selectbox("Choose Status", df['status'].unique())

    # Filter data
    filtered_df = df[df['status'] == status]

    # Show filtered table
    st.subheader(f"Status Data: {status}")
    st.dataframe(filtered_df)
    
except Exception as e:
    st.error(f"❌ Something went wrong: {e}")

import plotly.express as px

# Bar chart: total sales by product
st.subheader("📦 Total Sales by Product")
fig = px.bar(
    filtered_df,
    x='product',
    y='total_sales',
    color='status',
    title=f"Sales Breakdown by Product in {region}"
)
st.plotly_chart(fig, use_container_width=True)

from utils.insights import generate_insight

st.subheader("🔍 AI Insight")
st.info(generate_insight(filtered_df))
