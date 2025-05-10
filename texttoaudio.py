import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Google TTS App", layout="centered")
st.title("🗣️ Text-to-Speech with Google TTS")

text_input = st.text_area("Enter the text you want to convert to speech:", height=150)
lang = st.selectbox("Select language", ["en", "hi", "fr", "es", "de", "ta"])
submit = st.button("🎤 Convert to Speech")

if submit:
    if not text_input.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Generating speech..."):
            tts = gTTS(text=text_input, lang=lang)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                audio_path = fp.name

        st.success("✅ Speech generated!")
        st.audio(audio_path, format="audio/mp3")
