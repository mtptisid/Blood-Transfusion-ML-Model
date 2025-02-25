import streamlit as st
import numpy as np
import joblib

# Load saved model and scaler
model = joblib.load("blood_donation_model.pkl")
scaler = joblib.load("scaler.pkl")

# Streamlit UI
st.title("🩸 Blood Donation Prediction App")
st.write("Enter your details to check if you are likely to donate blood.")

# Input fields
recency = st.number_input("Recency (Months since last donation)", min_value=0, step=1)
frequency = st.number_input("Frequency (Total number of donations)", min_value=0, step=1)
monetary = st.number_input("Monetary (Total blood donated in c.c.)", min_value=0, step=250)
time = st.number_input("Time (Months since first donation)", min_value=0, step=1)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[recency, frequency, monetary, time]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.success("✅ Likely to donate blood!")
    else:
        st.error("❌ Not likely to donate blood.")