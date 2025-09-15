import streamlit as st
import pickle
import numpy as np

# Load trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Streamlit App
st.set_page_config(page_title="💧 Water Quality Prediction", layout="centered")

st.title("💧 Water Quality Potability Prediction")
st.markdown("""
This app predicts whether water is **Safe to Drink** or **Not Safe** based on chemical properties.  
Please enter the values below:
""")

# Input fields
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input("Hardness", min_value=0.0, step=0.1)
solids = st.number_input("Solids (ppm)", min_value=0.0, step=1.0)
chloramines = st.number_input("Chloramines", min_value=0.0, step=0.1)
sulfate = st.number_input("Sulfate", min_value=0.0, step=0.1)
conductivity = st.number_input("Conductivity", min_value=0.0, step=0.1)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0, step=0.1)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, step=0.1)
turbidity = st.number_input("Turbidity", min_value=0.0, step=0.1)

# Prediction button
if st.button("🔍 Check Water Quality"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity,
                          organic_carbon, trihalomethanes, turbidity]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]

    if prediction == 1:
        st.success("✅ The Water is **Safe to Drink** (Potable)")
    else:
        st.error("❌ The Water is **Not Safe to Drink** (Non-Potable)")