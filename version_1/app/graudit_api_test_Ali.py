from flask import Flask, request, jsonify
import docker
import zipfile
import os
import subprocess
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
client = docker.from_env()

@app.route('/endpoint', methods=['POST'])
def scan_code():
    # Check if file is present in request
    if 'file' not in request.files:
        raise BadRequest("File not present in request")
    
    project_zip = request.files['file']

    # Check if the file is a zip file
    if not zipfile.is_zipfile(project_zip):
        raise BadRequest("Invalid .zip file")
    
    project_zip.save("/app/project.zip")

    try:
        # Extract the zip file to the app directory
        with zipfile.ZipFile('/app/project.zip', 'r') as zip_ref:
            zip_ref.extractall('/app/code')
    except zipfile.BadZipFile:
        raise BadRequest("Invalid .zip file")

    # Run Graudit on the extracted code
    graudit_output = subprocess.run(["graudit", "/app/code"], capture_output=True, text=True)

    if graudit_output.returncode != 0:
        return jsonify({"error": f"Graudit error: {graudit_output.stderr}"}), 500

    graudit_results = {}
    
    # Parse the Graudit output into a JSON object
    lines = graudit_output.stdout.split("\n")
    for i, line in enumerate(lines):
        graudit_results[i] = line

    return jsonify(graudit_results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
