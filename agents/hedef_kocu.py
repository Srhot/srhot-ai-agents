import streamlit as st
from model_utils import generate_response

def run(user_input):
    st.subheader("🎯 Hedef Koçu Modu")
    prompt = f"""Sen bir 🎯 hedef koçu modusun. Kullanıcı sana şöyle dedi: '{user_input}'. Ona destek ol:"""
    response = generate_response(prompt)
    st.write(response)
