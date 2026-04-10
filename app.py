import streamlit as st
from model import predict
from utils import explain_result

st.title("🧠 Personalized Healthcare Guidance System")

st.write("Enter your blood test values:")

hb = st.number_input("Hemoglobin", value=12.0)
wbc = st.number_input("WBC Count", value=8000)
platelets = st.number_input("Platelets", value=250000)
rbc = st.number_input("RBC", value=5.0)

if st.button("Analyze Report"):
    result = predict([hb, wbc, platelets, rbc])
    
    st.success(f"🩺 Predicted Condition: {result}")
    
    explanation = explain_result(result)
    st.info(f"💡 Guidance: {explanation}")
