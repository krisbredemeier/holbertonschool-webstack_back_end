#!/usr/bin/python3

'''
You will implement now all routes for accessing to User instances:

List all User
Get one User
Delete one User
Create one User
Update one User
'''

from flask import Flask
from flask import request
from flask import jsonify
from appi.v1.views import app_views
from models import User
from models import db_session

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def access_user():
    '''
    list of user
    '''
    users = []
    for user in User.all():
        users.append(user.to_dict())
    return jsonify(users)
