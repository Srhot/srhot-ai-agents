import streamlit as st
from model_utils import generate_response

def run(user_input):
    st.subheader("🔍 Araştırma Ortağı Modu")
    prompt = f"""Sen bir 🔍 araştırma ortağı modusun. Kullanıcı sana şöyle dedi: '{user_input}'. Ona destek ol:"""
    response = generate_response(prompt)
    st.write(response)
