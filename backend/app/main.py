from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app= Flask(__name__)
CORS(app)

@app.route('/getData', methods=['GET', 'POST'])
def index():
    data = request.get_json()
    print("DATA", data)
    exportLink = data['exportLink']
    req = requests.get(exportLink)
    url_content = req.content
    decode_data = url_content.decode('utf-8')
    result = {
        "csv_content": decode_data
    }
    return jsonify(result)

  