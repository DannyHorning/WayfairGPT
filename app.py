from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
openai.api_key = openai_api_key

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Replace with your actual model ID
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=150
    )
    return jsonify({'response': response.choices[0]['message']['content'].strip()})

if __name__ == '__main__':
    app.run(debug=True)
