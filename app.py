# -*- coding: utf-8 -*-
"""
Streamlit Air Pollution Prediction App
"""

import streamlit as st
import numpy as np
import pickle
import os

# ---- Load your trained model safely ----
# This works both locally and on Streamlit Cloud
model_path = os.path.join(os.path.dirname(__file__), "Pollution_Model.pkl")

if not os.path.exists(model_path):
    st.error("❌ Model file 'Pollution_Model.pkl' not found.")
    st.info("Make sure the model file is uploaded in the same folder as app.py in your GitHub repo.")
    st.stop()

with open(model_path, "rb") as file:
    model = pickle.load(file)

# ---- App title ----
st.title("🌍 Air Pollution Prediction System")
st.markdown("Predict the **Air Quality Index (AQI)** using key air quality parameters.")

# ---- Input fields ----
st.header("Enter Air Quality Parameters")

col1, col2 = st.columns(2)

with col1:
    aqi_value = st.number_input("Overall AQI Value", min_value=0.0)
    aqi_category = st.selectbox("Overall AQI Category", ["Good", "Moderate", "Unhealthy", "Very Unhealthy", "Hazardous"])
    co_aqi_value = st.number_input("CO AQI Value", min_value=0.0)
    co_aqi_category = st.selectbox("CO AQI Category", ["Good", "Moderate", "Unhealthy", "Very Unhealthy", "Hazardous"])
    ozone_aqi_value = st.number_input("Ozone AQI Value", min_value=0.0)

with col2:
    ozone_aqi_category = st.selectbox("Ozone AQI Category", ["Good", "Moderate", "Unhealthy", "Very Unhealthy", "Hazardous"])
    no2_aqi_value = st.number_input("NO₂ AQI Value", min_value=0.0)
    no2_aqi_category = st.selectbox("NO₂ AQI Category", ["Good", "Moderate", "Unhealthy", "Very Unhealthy", "Hazardous"])
    pm25_aqi_value = st.number_input("PM2.5 AQI Value", min_value=0.0)

# ---- Predict button ----
if st.button("Predict Air Quality Index"):

    # ---- Encode categorical text fields ----
    encoding_map = {
        "Good": 0,
        "Moderate": 1,
        "Unhealthy": 2,
        "Very Unhealthy": 3,
        "Hazardous": 4
    }

    # Convert categories to numeric and create numpy array
    input_array = np.array([
        aqi_value,
        encoding_map[aqi_category],
        co_aqi_value,
        encoding_map[co_aqi_category],
        ozone_aqi_value,
        encoding_map[ozone_aqi_category],
        no2_aqi_value,
        encoding_map[no2_aqi_category],
        pm25_aqi_value
    ]).reshape(1, -1)

    # ---- Prediction ----
    try:
        prediction = model.predict(input_array)
        aqi_pred = prediction[0]

        st.subheader(f"Predicted Air Quality Index (AQI): {aqi_pred:.2f}")

        # ---- Color-coded AQI category ----
        if aqi_pred <= 50:
            st.success("Air Quality: Good 🟩")
        elif aqi_pred <= 100:
            st.warning("Air Quality: Moderate 🟨")
        elif aqi_pred <= 150:
            st.error("Air Quality: Unhealthy for Sensitive Groups 🟧")
        elif aqi_pred <= 200:
            st.error("Air Quality: Unhealthy 🟥")
        elif aqi_pred <= 300:
            st.error("Air Quality: Very Unhealthy 🟪")
        else:
            st.error("Air Quality: Hazardous 🟫")

    except Exception as e:
        st.error(f"⚠️ Model prediction failed: {e}")
        st.write("Check that your input matches the features the model was trained on.")

# ---- Footer ----
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Developed by: NTAKIRUTIMANA Patrick | RP TUMBA | ETT B-Tech 2025–2026")
