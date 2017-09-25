#!/usr/bin/python3
'''
documenation
'''
from flask import Flask
from flask import jsonify
from api.v1.views import app_views
from models import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def test():
    '''
    runs quick test on status
    '''
    return '{"status" : "OK"}'


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def database_stats():
    '''
    link database to routes and count number of users
    '''
    return jsonify(users=User.count())
