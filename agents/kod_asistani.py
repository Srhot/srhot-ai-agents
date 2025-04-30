import streamlit as st
from model_utils import generate_response

def run(user_input):
    st.subheader("🧰 Kod Asistanı Modu")
    prompt = f"""Sen bir 🧰 kod asistanı modusun. Kullanıcı sana şöyle dedi: '{user_input}'. Ona destek ol:"""
    response = generate_response(prompt)
    st.write(response)
