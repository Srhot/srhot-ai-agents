import streamlit as st
import os
from dotenv import load_dotenv
import openai

# ENV
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Agent tanımları
def kod_partneri_agent(prompt):
    system_message = """Sen bir Kod Partnerisin. Görevin kullanıcının verdiği kodu analiz etmek, düzeltmek, refactor etmek ve test senaryoları önermektir."""
    return gpt_response(system_message, prompt)

def prompt_atolyesi_agent(prompt):
    system_message = """Sen bir Prompt Mühendisliği Uzmanısın. Kullanıcının verdiği fikri daha etkili hale getirmek için ileri düzey prompt önerileri yap."""
    return gpt_response(system_message, prompt)

def gpt_response(system_prompt, user_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4", messages=messages, temperature=0.7
    )
    return response['choices'][0]['message']['content']

# UI
st.set_page_config(page_title="Srhot AI Agents", layout="wide")
st.title("🤖 Srhot'ın Kişisel AI Asistanları")

st.sidebar.header("Modül Seç")
agent_type = st.sidebar.selectbox("Bir görev seç:", ["Kod Partneri", "Prompt Atölyesi"])

prompt = st.text_area("📝 Komutunuzu yazın:", height=200)
submit = st.button("Çalıştır")

if submit and prompt.strip() != "":
    with st.spinner("Yanıt oluşturuluyor..."):
        if agent_type == "Kod Partneri":
            result = kod_partneri_agent(prompt)
        elif agent_type == "Prompt Atölyesi":
            result = prompt_atolyesi_agent(prompt)

        st.markdown("### 🎯 Yanıt:")
        st.code(result, language='markdown')
