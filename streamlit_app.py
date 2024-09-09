import streamlit as st
import pandas as pd

# Set up custom color scheme
st.set_page_config(page_title="Payment Profile Visualizer", page_icon="💰", layout="centered")
st.markdown(
    """
    <style>
    :root {
        --primary-color: #1f493b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("Payment Profile Visualizer")

# Input form
recurring_payment = st.number_input("Recurring payment (DKK):", min_value=0, step=500)
upfront_payment = st.number_input("Upfront payment (DKK):", min_value=0, step=500)
duration = st.selectbox("Duration (in quarters):", [20, 40])

# Generate the DataFrame
quarters = list(range(1, duration + 1))
payments = [3*recurring_payment] * duration
payments[0] += upfront_payment  # Add the upfront payment to the first quarter

df = pd.DataFrame([payments], columns=[f"Q{i}" for i in quarters], index=["Payment"])

# Display the DataFrame
st.subheader("Payment Schedule")
st.dataframe(df)

# Visualize the payment profile
st.subheader("Payment Profile Visualization")
st.bar_chart(df.T)  # Transpose the DataFrame for correct bar chart orientation
