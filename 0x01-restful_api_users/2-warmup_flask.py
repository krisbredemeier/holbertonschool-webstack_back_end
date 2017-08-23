#!/usr/bin/python3

from flask import Flask
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')

@app.route('/', methods=['GET'])
def run_flask():
    '''
    start flask application
    '''
    return "Holberton School"

@app.route('/c', methods=['GET'])
def retunC():
    return "C is fun!"

if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
