#!/usr/bin/python3

'''
The listening port must be the value of the environment variable HBNB_API_PORT
The IP bound to must be the value of the environment variable HBNB_API_HOST
GET /hbtn must return JSON data:
Content-Type: application/json
Representation of the dictionary: tips:
"C" = "is fun"
"Python" = "is cool"
"Sysadmin" = "is hiring"
You must use the option strict_slashes=False in your route definition
Your code should not be executed when imported
(by using if __name__ == "__main__":)
'''

from flask import Flask
from flask import jsonify
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')


@app.route('/hbtn', methods=['GET'])
def get_hbtn_data():
    '''
    get hbtn route
    '''
    return jsonify(C="is fun",Python="is cool", Sysadmin="is hiring")


if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
