import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def calculate_payment_profile(recurring_payment, upfront_payment, duration):
    quarters = 40
    if duration == "20 Quarters":
        quarters = 20

    data = {f"Q{q}": [recurring_payment if i > 0 else recurring_payment + upfront_payment] for i, q in enumerate(range(1, quarters + 1))}
    df = pd.DataFrame(data)
    return df

st.title("Payment Profile Calculator")

recurring_payment = st.number_input("Recurring payment (DKK)", min_value=0.0, step=100.0)
upfront_payment = st.number_input("Upfront payment (DKK)", min_value=0.0, step=100.0)
duration = st.selectbox("Duration", ["20 Quarters", "40 Quarters"])

if st.button("Calculate Payment Profile"):
    payment_df = calculate_payment_profile(recurring_payment, upfront_payment, duration)
    st.dataframe(payment_df)

    fig, ax = plt.subplots(figsize=(12, 6))
    payment_df.plot(kind="bar", ax=ax)
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Payment (DKK)")
    ax.set_title("Payment Profile")
    st.pyplot(fig)
