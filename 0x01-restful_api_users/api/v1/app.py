#!/usr/bin/python3
'''
documenation
'''
from flask import Flask
from flask import Blueprint
from flask import jsonify
from api.v1.views import app_views
import os
from models import db_session
app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    '''
    error handleler
    '''
    return jsonify(error="Not found"), 404


@app.teardown_appcontext
def close_db(error):
    '''
    Closes the database again at the end of the request.
    '''
    db_session.remove()


if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
