#!/usr/bin/python3

'''
documenation
'''

from flask import Flask
from flask import jsonify
from api.v1.views import app_views
from models import User
from models import db_session


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_code():
    '''
    runs quick test on status
    '''
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def database_stats():
    '''
    link database to routes and count number of users
    '''
    user = db_session.query(User).get(all)
    return jsonify(users=user)
