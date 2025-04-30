
import streamlit as st
import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Srhot AI Agents", layout="wide")
st.title("🧠 Srhot AI Agents")

agent_type = st.selectbox("Agent rolünü seçin:", ["🎯 Hedef Koçu", "🧰 Kod Asistanı", "🔍 Araştırma Ortağı", "📚 Bilgi Yöneticisi", "⏱️ Zaman Yöneticisi"])
user_input = st.text_area("🔤 Sorunuzu yazın:")

def agent_prompt(role, question):
    system_prompts = {
        "🎯 Hedef Koçu": "Sen bir hedef koçusun. Kullanıcının kısa, orta ve uzun vadeli hedeflerini belirlemesine ve takip etmesine yardımcı ol.",
        "🧰 Kod Asistanı": "Sen ileri düzey bir yazılım geliştirici asistanısın. Kullanıcının kodlarını analiz et, iyileştir ve açıklamalar yap.",
        "🔍 Araştırma Ortağı": "Sen güvenilir bir araştırma partnerisin. Soruları kaynaklara dayalı şekilde kısa ve net özetle.",
        "📚 Bilgi Yöneticisi": "Sen bir bilgi yönetimi uzmanısın. Kullanıcının notlarını düzenlemesine, ilişkilendirmesine ve bilgi mimarisi kurmasına yardım et.",
        "⏱️ Zaman Yöneticisi": "Sen bir zaman yönetimi asistanısın. Kullanıcının zaman blokları oluşturmasına, plan yapmasına yardım et."
    }
    return [{"role": "system", "content": system_prompts[role]},
            {"role": "user", "content": question}]

if st.button("Yanıtla") and user_input:
    with st.spinner("Yanıt oluşturuluyor..."):
        messages = agent_prompt(agent_type, user_input)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7
        )
        st.markdown("### ✅ Yanıt:")
        st.write(response.choices[0].message["content"])
