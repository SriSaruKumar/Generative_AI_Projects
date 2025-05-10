from flask import Flask, request, jsonify
from phi.agent import Agent
from phi.model.cohere import CohereChat
from phi.tools.duckduckgo import DuckDuckGo
import os

# Set your Cohere API key
os.environ["COHERE_API_KEY"] = "FNFxNAh6yNK5K0I1ykt0oqOFe4j4sOAEdqhIWsMx"

# Create the agent using Cohere
web_agent = Agent(
    name="Web Agent",
    model=CohereChat(id="command-r-plus"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Initialize Flask app
app = Flask(__name__)

# Route for the prompt input and response
@app.route('/ask', methods=['POST'])
def ask_prompt():
    # Get the user's prompt from the POST request
    user_prompt = request.json.get('prompt')
    
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    # Get the response from the agent
    try:
        response = web_agent.print_response(user_prompt, stream=False)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
