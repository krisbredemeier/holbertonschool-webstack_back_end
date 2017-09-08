#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def test():
    '''
    runs quick test on status
    '''
    return '{"status" : "OK"}'

def database():
    '''
    link database to routs and count number of users
    '''
    # User.count()
    return jsonify(users="number of users in database")
