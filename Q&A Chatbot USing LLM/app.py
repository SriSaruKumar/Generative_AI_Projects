import streamlit as st
import cohere

# Initialize Cohere client (Replace 'YOUR_API_KEY' with your actual API key)
COHERE_API_KEY = "FNFxNAh6yNK5K0I1ykt0oqOFe4j4sOAEdqhIWsMx"
co = cohere.Client(COHERE_API_KEY)

# Set Streamlit page config
st.set_page_config(page_title="Q&A Chatbot")

# App header
st.header("Cohere-Powered Chatbot")

# User input
user_input = st.text_input("Ask a question:", key="input")

# Function to get response from Cohere
def get_cohere_response(question):
    response = co.generate(
        model="command",  # Use "command" or "command-r-plus" for better results
        prompt=question,
        max_tokens=100
    )
    return response.generations[0].text.strip()

# Submit button
submit = st.button("Get Answer")

# If submit button is clicked
if submit and user_input:
    response = get_cohere_response(user_input)
    st.subheader("Response:")
    st.write(response)
