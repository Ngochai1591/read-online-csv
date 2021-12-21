from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import requests
import ujson as json
import gzip


app= Flask(__name__)
CORS(app)

# @app.route('/getData', methods=['GET', 'POST'])
# def index():
#     data = request.get_json()
#     print("DATA", data)
#     exportLink = data['exportLink']
#     req = requests.get(exportLink)
#     url_content = req.content
#     decode_data = url_content.decode('utf-8')
#     result = {
#         "csv_content": decode_data
#     }
#     return jsonify(result)


@app.route('/getData', methods=['GET', 'POST'])
def index():
    data = request.get_json()
    print("DATA", data)
    exportLink = data['exportLink']
    req = requests.get(exportLink)
    url_content = req.content
    decode_data = url_content.decode('utf-8')

    compression_level = 9  # of 9 max
    content = gzip.compress(url_content, compression_level)
    response = make_response(content)
    response.headers['Content-length'] = len(content)
    response.headers['Content-Encoding'] = 'gzip'
    return response
  