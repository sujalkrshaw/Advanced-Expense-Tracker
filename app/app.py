import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.preprocessing import load_data
from src.analysis import category_analysis, monthly_analysis
from src.model import predict

# Load data
df = load_data()

# ----------------------------
# SIDEBAR FILTER
# ----------------------------
st.sidebar.header("🔍 Filter Data")

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df['category'].unique())
)

if selected_category != "All":
    df = df[df['category'] == selected_category]

# ----------------------------
# HEADER
# ----------------------------
st.markdown("# 💰 Advanced Expense Tracker")
st.markdown("### 📊 Smart Financial Analytics Dashboard")

# ----------------------------
# TABS
# ----------------------------
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📈 Analysis", "🔮 Prediction"])

# ============================
# TAB 1 — DASHBOARD
# ============================
with tab1:
    st.markdown("## 📊 Overview")

    col1, col2, col3 = st.columns(3)

    total = df['amount'].sum()
    avg = df['amount'].mean()
    max_spend = df['amount'].max()

    col1.metric("💰 Total Spending", f"₹{total:.0f}")
    col2.metric("📊 Avg Transaction", f"₹{avg:.0f}")
    col3.metric("🔥 Max Expense", f"₹{max_spend:.0f}")

# ============================
# TAB 2 — ANALYSIS
# ============================
with tab2:
    st.markdown("## 📈 Data Analysis")

    col1, col2 = st.columns(2)

    # Category Chart
    with col1:
        st.subheader("📊 Category Analysis")
        cat = category_analysis(df)
        st.bar_chart(cat)

    # Monthly Trend
    with col2:
        st.subheader("📈 Monthly Trend")
        month = monthly_analysis(df)
        st.line_chart(month)

# ============================
# TAB 3 — PREDICTION
# ============================
with tab3:
    st.markdown("## 🔮 Expense Prediction")

    month_input = st.slider("Select Month", 1, 12)

    prediction = predict(month_input)

    st.success(f"Predicted Expense: ₹{prediction:.2f}")