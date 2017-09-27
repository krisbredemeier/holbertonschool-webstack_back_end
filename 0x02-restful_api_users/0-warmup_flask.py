#!/usr/bin/python3

'''
Listening on the port 5000, bound publically (0.0.0.0)
GET / must return "Holberton School"
You must use the option strict_slashes=False in your route definition
Your code should not be executed when imported
(by using if __name__ == "__main__":)
'''

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def run_flask():
    '''
    start flask application
    '''
    app.url_map.strict_slashes = False
    return "Holberton School"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
