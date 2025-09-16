from flask import Flask, request, jsonify
from model.chatbot_model import get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    response = get_response(message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=5000)
