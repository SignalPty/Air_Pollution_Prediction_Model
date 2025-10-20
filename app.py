# -*- coding: utf-8 -*-
"""
Streamlit Air Pollution Prediction App (Using pickle)
"""

import streamlit as st
import numpy as np
import pickle
import os

# ---- Load model safely ----
@st.cache_resource
def load_model():
    model_path = "Air_Pollution_Model.pkl"  # relative path
    if not os.path.exists(model_path):
        st.error(f"❌ Model file not found: {model_path}")
        return None
    try:
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        return model
    except ModuleNotFoundError as e:
        st.error("⚠️ Missing library required to load the model.")
        st.write(f"Details: {e}")
        return None
    except Exception as e:
        st.error("⚠️ Failed to load the model.")
        st.write(f"Details: {e}")
        return None

# Load the model
model = load_model()

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
    no2_aqi_category = st.selectbox("NO₂ AQI
