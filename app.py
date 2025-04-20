# app.py
from flask import Flask, request, jsonify
from autogen_worker import analyze_code  # Import your worker

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    results = analyze_code(code)  # Call AutoGen
    return jsonify({"issues": results})