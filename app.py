from flask import Flask, request, jsonify, render_template, send_from_directory
from datetime import datetime
import json
import os
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Use environment variable for secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-this')

# Ensure the response file is stored in a writable directory
RESPONSE_FILE = os.path.join(os.environ.get('RESPONSE_DIR', '.'), 'response.json')

@app.before_request
def before_request():
    if os.environ.get('FLASK_ENV') == 'production':
        # Redirect to HTTPS in production
        if request.url.startswith('http://'):
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)

# ... rest of your routes remain the same ...

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_ENV') != 'production')
