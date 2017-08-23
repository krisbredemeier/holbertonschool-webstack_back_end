#!/usr/bin/python3

from flask import Flask

def run_flask():
    '''
    start flask application
    '''
    app = Flask(__name__)
    # app.run(host='34.206.234.184', port=35129)
    # app.url_map.strict_slashes = False
    # print("Holberton")
    app.run(host='0.0.0.0', port=5000, strict_slashes=False)
    app.url_map.strict_slashes = False
    print("Holberton")

if __name__ == "__main__":
    run_flask()
