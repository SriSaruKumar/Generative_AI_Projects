import streamlit as st
import cohere

# Set up your Cohere API key
COHERE_API_KEY = "FNFxNAh6yNK5K0I1ykt0oqOFe4j4sOAEdqhIWsMx"  # Replace this with your actual key
co = cohere.Client(COHERE_API_KEY)

# Streamlit UI
st.set_page_config(page_title="Text Summarizer")
st.title("Text Summarizer with Cohere")

# Text input
input_text = st.text_area("Enter the text you want to summarize:", height=200)

# Summarize button
if st.button("Summarize") and input_text.strip():
    with st.spinner("Generating summary..."):
        response = co.summarize(
            text=input_text,
            model='summarize-xlarge',  # Use Cohere's summarization model
            length='medium',           # Options: 'short', 'medium', 'long'
            format='paragraph',        # Options: 'paragraph', 'bullets'
            extractiveness='auto'      # Options: 'low', 'medium', 'high', 'auto'
        )
        summary = response.summary
        st.subheader("Summary:")
        st.write(summary)
