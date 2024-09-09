import streamlit as st
import pandas as pd

# Custom CSS
st.set_page_config(page_title="Payment Profile Calculator")

st.markdown(
    f"""
    <style>
    .stButton button {{
        background-color: #1f493b !important;
        color: white !important;
        border-radius: 0px !important;
        padding: 0.5rem 1.5rem !important;
        font-size: 1rem !important;
        border: none !important;
    }}
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
quarters = [f"Q{i}" for i in range(1, duration + 1)]
payments = [recurring_payment] * duration
payments[0] += upfront_payment  # Add the upfront payment to the first quarter

df = pd.DataFrame([payments], columns=quarters, index=["Payment"])

# Ensure quarters are sorted correctly for visualization
df = df.T  # Transpose for easier plotting
df.index = pd.Categorical(df.index, categories=quarters, ordered=True)  # Sort correctly by quarter
df = df.sort_index()

# Display the DataFrame
st.subheader("Payment Schedule")
st.dataframe(df.T)  # Display the original format

# Visualize the payment profile
st.subheader("Payment Profile Visualization")
st.bar_chart(df)
