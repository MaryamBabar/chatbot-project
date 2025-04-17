from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('user_input')

    # Dummy response logic
    response = f"You said: {user_input}. I'm just a basic bot for now 🤖"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
