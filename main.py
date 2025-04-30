import streamlit as st
from agents import hedef_kocu, kod_asistani, bilgi_yoneticisi, zaman_yoneticisi, arastirma_ortagi

st.set_page_config(page_title="Srhot AI Asistan", layout="centered")
st.title("🧠 Srhot Kişisel AI Asistanı")

user_input = st.text_area("🔍 Komut ver:", placeholder="Örn: 'Bugünkü hedefimi yazmak istiyorum.'")

if user_input:
    if "hedef" in user_input.lower():
        hedef_kocu.run(user_input)
    elif "kod" in user_input.lower():
        kod_asistani.run(user_input)
    elif "bilgi" in user_input.lower():
        bilgi_yoneticisi.run(user_input)
    elif "zaman" in user_input.lower() or "plan" in user_input.lower():
        zaman_yoneticisi.run(user_input)
    elif "araştır" in user_input.lower() or "teknoloji" in user_input.lower():
        arastirma_ortagi.run(user_input)
    else:
        st.warning("Komutu anlayamadım. 'hedef', 'kod', 'bilgi', 'zaman' veya 'araştırma' anahtarlarını kullan.")
