import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("💧 Water Potability Prediction App")
st.write("Enter the following water quality parameters:")

# Input fields
ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input("Hardness", step=0.1)
solids = st.number_input("Total Dissolved Solids", step=1.0)
chloramines = st.number_input("Chloramines", step=0.1)
sulfate = st.number_input("Sulfate", step=0.1)
conductivity = st.number_input("Conductivity", step=0.1)
organic_carbon = st.number_input("Organic Carbon", step=0.1)
trihalomethanes = st.number_input("Trihalomethanes", step=0.1)
turbidity = st.number_input("Turbidity", step=0.1)

if st.button("Check Potability"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate,
                          conductivity, organic_carbon, trihalomethanes, turbidity]])
    features = scaler.transform(features)
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.success("✅ Water is Potable (Safe to Drink)")
    else:

        st.error("❌ Water is Not Potable (Unsafe to Drink)")

import pickle

# model save
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# scaler save
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)
