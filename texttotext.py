import streamlit as st
import cohere

# Set your Cohere API key
api_key = "bujU8MGyFDCKtqFxIA4QYphgtmSaJH6BcsfKUczR"
co = cohere.Client(api_key)

# Streamlit UI
st.title("Text-to-Text with Cohere")

# Text input field
prompt = st.text_area("Enter your prompt")

# Dropdown for choosing the task
task = st.selectbox("Choose task", ["Summarize", "Generate", "Paraphrase"])

if st.button("Generate"):
    with st.spinner("Processing..."):
        if task == "Summarize":
            response = co.generate(
                model="summarize-xlarge",
                prompt=f"Summarize this: {prompt}",
                max_tokens=100
            )
        elif task == "Generate":
            response = co.generate(
                model="command",
                prompt=prompt,
                max_tokens=150
            )
        elif task == "Paraphrase":
            response = co.generate(
                model="command",
                prompt=f"Paraphrase this: {prompt}",
                max_tokens=100
            )
        
        # Display response
        st.subheader("Response:")
        st.write(response.generations[0].text)
