#!/usr/bin/python3

from flask import Flask
from flask import jsonify
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')

@app.route('/', methods=['GET'])
def get_holberton():
    '''
    start flask application
    '''
    return "Holberton School"

@app.route('/c', methods=['GET'])
def get_C():
    return "C is fun!"

@app.route('/hbtn', methods=['GET'])
def get_hbtn_data():
    return jsonify(C="is fun",
                    Python="is cool",
                    Sysadmin="is hiring")

if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
