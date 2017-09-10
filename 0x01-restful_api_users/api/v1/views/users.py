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
from api.v1.views import app_views
from models import User
from models import db_session
from flask import abort

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def access_user():
    '''
    list of user
    '''
    users = []
    for user in User.all():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<udrt_id>', methods=['GET'], strict_slashes=False)
def user(user_id):
    '''
    update get
    '''
    user = User.get(user_id)
    if user is None:
        return abort(404)
    else:
        return jsonify(user.to_dict())


@app_views.route('/users/<udrt_id>', methods=['GET'], strict_slashes=False)
def delete(user_id):
    '''
    manages delete
    '''
    user = User.get(user_id)
    if user is None:
        return abort(404)
    else:
        db_session.delete(user)
        sb_session.commit()
        return jsonify()
