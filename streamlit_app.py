import streamlit as st
import pandas as pd

# App title
st.title("Payment Profile Visualizer")

# Input form
recurring_monthly_payment = st.number_input("Recurring monthly payment (DKK):", min_value=0, step=500)
upfront_payment = st.number_input("Upfront payment (DKK):", min_value=0, step=500)

# Define duration options with labels and underlying values
duration_options = [("5 years", 20), ("10 years", 40)]

# Use the selectbox with format_func to show labels
duration = st.selectbox(
    "Duration:",
    options=duration_options,
    format_func=lambda x: x[0]
)[1]  # Get the underlying value for calculation

# Calculate quarterly payment from monthly payment
recurring_quarterly_payment = recurring_monthly_payment * 3

# Generate the DataFrame
quarters = [f"Q{i}" for i in range(1, duration + 1)]
payments = [recurring_quarterly_payment] * duration
payments[0] += upfront_payment  # Add the upfront payment to the first quarter

df = pd.DataFrame([payments], columns=quarters, index=["Payment"])

# Ensure quarters are sorted correctly for visualization
df = df.T  # Transpose for easier plotting
df.index = pd.Categorical(df.index, categories=quarters, ordered=True)  # Sort correctly by quarter
df = df.sort_index()

# Display the DataFrame with increased width
st.subheader("Payment Schedule")
st.dataframe(df.T, use_container_width=True)  # Set use_container_width to True

# Visualize the payment profile
st.subheader("Payment Profile Visualization")
st.bar_chart(df)
