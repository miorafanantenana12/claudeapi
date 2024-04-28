from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def get_response(question):
    api_key = "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"
    endpoint = "https://azeu-api-beta.onrender.com/GlobalGPT"
    params = {"question": question, "apiKey": api_key}

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch response."}

@app.route('/')
def index():
    return 'Hello, please go to /ask to ask a question.'

@app.route('/ask', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        question = request.form.get('question')
    elif request.method == 'GET':
        question = request.args.get('question')
    else:
        return 'Unsupported method.'

    if question:
        response = get_response(question)
        return jsonify(response)
    else:
        return 'Please provide a question.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
