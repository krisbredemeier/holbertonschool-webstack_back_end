#!/usr/bin/python3
from flask import Flask
from api.v1.views import app_views
app = Flask(__name__)

app.register_blueprint(api.v1.app_views, url_prefix='/api/v1')

if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
