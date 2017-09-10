#!/usr/bin/python3

'''
The listening port must be the value of the environment variable HBNB_API_PORT
The IP bound to must be the value of the environment variable HBNB_API_HOST
GET / must return "Holberton School"
GET /c must return "C is fun!"
You must use the option strict_slashes=False in your route definition
Your code should not be executed when imported
(by using if __name__ == "__main__":)
'''

from flask import Flask
import os

app = Flask(__name__)
HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')


@app.route('/', methods=['GET'], strict_slashes=False)
def run_flask():
    '''
    start flask application
    '''
    return "Holberton School"


@app.route('/c', methods=['GET'], strict_slashes=False)
def retunC():
    return "C is fun!"


if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
