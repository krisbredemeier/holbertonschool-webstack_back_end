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

from flask import request
from flask import abort
app = Flask(__name__)

HBNB_API_PORT = os.environ.get('HBNB_API_PORT')
HBNB_API_HOST = os.environ.get('HBNB_API_HOST')
app.register_blueprint(app_views)

if os.environ.get("HBNB_YELP_AUTH") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    auth = Auth()

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
    request.current_user = auth.current_user(request)
    if not auth.require_auth(
        request.path,
        ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    ):
        return None
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT)
