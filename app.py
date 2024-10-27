from flask import Flask, request, jsonify, render_template, send_from_directory
from datetime import datetime
import json
import os

app = Flask(__name__)

# Configuration for file paths
RESPONSE_FILE = 'response.json'
VIDEO_FOLDER = 'static/videos'  # Folder for storing videos

# Create videos directory if it doesn't exist
os.makedirs(VIDEO_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/happy')
def happy():
    return render_template('happy.html')

@app.route('/sad')
def sad():
    return render_template('sad.html')

@app.route('/checker')
def checker():
    return render_template('checker.html')

@app.route('/save_response', methods=['POST'])
def save_response():
    data = request.json
    response_data = {
        'response': data.get('response'),
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    with open(RESPONSE_FILE, 'w') as f:
        json.dump(response_data, f)
    
    return jsonify({'status': 'success'})

@app.route('/check_response')
def check_response():
    if os.path.exists(RESPONSE_FILE):
        with open(RESPONSE_FILE, 'r') as f:
            response_data = json.load(f)
        return jsonify(response_data)
    return jsonify({'response': None})

if __name__ == '__main__':
    app.run(debug=True)