from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_basicauth import BasicAuth
import hashlib
import os
import shutil
import zipfile
import subprocess

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'secret'

basic_auth = BasicAuth(app)
limiter = Limiter(app, default_limits=["200 per day", "50 per hour"])

@app.route('/md5', methods=['POST'])
@basic_auth.required
@limiter.limit("20 per minute")
def hash_data():
    content = request.get_json()
    data = content['data']
    hashed_data = hashlib.md5(data.encode()).hexdigest()
    return jsonify({'hashed_data': hashed_data})

@app.route('/endpoint', methods=['POST'])
@basic_auth.required
@limiter.limit("10 per minute")
def scan_code():
    file = request.files['file']
    file.save('/tmp/code.zip')
    with zipfile.ZipFile('/tmp/code.zip', 'r') as zip_ref:
        zip_ref.extractall('/tmp/code')
    result = subprocess.run(['graudit', '-B', '/tmp/code'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = result.stdout.decode('utf-8') if result.stdout else ""
    error = result.stderr.decode('utf-8') if result.stderr else ""
    print(f"Output: {output}")
    print(f"Error: {error}")

    shutil.rmtree('/tmp/code')
    output = result.stdout.decode()
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
