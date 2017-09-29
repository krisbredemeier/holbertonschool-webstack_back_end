#!/usr/bin/python3

'''
documenation
'''

from flask import Flask
from flask import jsonify
from flask import abort
from api.v1.views import app_views
from models import User
from models import db_session
from sqlalchemy import func
from sqlalchemy import distinct


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_code():
    '''
    runs quick test on status
    '''
    return jsonify({'status': "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def database_stats():
    '''
    link database to routes and count number of users
    '''

    users = db_session.query(User).count()
    return jsonify({'users': users})


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def raise_unauthorized():
    '''
    abort if unauthorized
    '''
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def raise_forbidden():
    '''
    abort if forbidden
    '''
    abort(403)
