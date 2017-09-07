#!/usr/bin/python3
from flask import Flask
from flask import Blueprint
from api.v1.views import app_views
import os
app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')

app.register_blueprint(app_views, url_prefix='/api/v1')

if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
