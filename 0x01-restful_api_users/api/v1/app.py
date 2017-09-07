#!/usr/bin/python3
from flask import Flask
from flask import Blueprint
from flask import jsonify
from api.v1.views import app_views
import os
app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')
app.register_blueprint(app_views)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Not found"), 404

if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
