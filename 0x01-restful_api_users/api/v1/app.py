#!/usr/bin/python3
from flask import Flask
from api.v1.views import app_views

app_views.register_blueprint(url_prefix='/api/v1')

if __name__ == "__main__":
    app_views.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
