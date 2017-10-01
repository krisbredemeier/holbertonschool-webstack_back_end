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
from api.v1.auth.auth import Auth
app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')
app.register_blueprint(app_views)

Auth = auth

list = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']

@app.errorhandler(404)
def page_not_found(e):
    '''
    error handleler not found
    '''
    return jsonify(error="Not found"), 404


@app.errorhandler(401)
def unauthorized(e):
    '''
    throws error if attempt is unauthorized
    '''
    return jsonify(error="Unauthorized"), 401


@app.errorhandler(403)
def forbidden(e):
    '''
    HTTP status code for a request where the user is authenticate
    but not allowed to access to a resource
    '''
    return jsonify(error="Forbidden"), 403


@app.teardown_appcontext
def close_db(error):
    '''
    Closes the database again at the end of the request.
    '''
    db_session.remove()

@app.before_request
def before_request():
    '''
    filter each request
    '''
    if request.path not in list:
        require_auth(auth)
    if auth.authorization_header(request)is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)



if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
