#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def run_flask():
    '''
    start flask application
    '''
    app.url_map.strict_slashes = False
    return "Holberton School"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


# app = Flask(__name__)
#
# @app.route('/', methods=['GET'])
# def test():
#     print("Holberton")
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)
