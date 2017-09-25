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
    user = db_session.query(User).order_by(User.created_at).all()
    if user is None:
        return abort(404)
    else:
        return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def user(user_id):
    '''
    update get
    '''
    user = db_session.query(User).get(user_id)
    if user is None:
        return abort(404)
    else:
        return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def delete_user(user_id):
    '''
    manages delete
    '''
    user = db_session.query(User).get(user_id)
    if user is None:
        return abort(404)
    else:
        db_session.delete(user)
        sb_session.commit()
        return jsonify()


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    '''
    creates a new user
    '''
    if request.get_json():
        json = request.get_json()
        email = json.get('email')
        if email is None:
            return jsonify(error='email missing'), 404
        password = json.get('password')
        if password is None:
            return jsonify(error='password missing'), 404
        new_user = User()
        new_user.email = json['email']
        new_user.password = json['password']
        if json.get('first_name'):
            new_user.first_name = json.get('first_name')
        if json.get('last_name'):
            new_user.first_name = json.get('last_name')
        try:
            db_session.add(new_user)
            db_session.commit()
        except:
            return jsonify(error="Can't create user: <exceptino message>"), 400
        return jsonify(User.last().to_dict()), 201
    else:
        return jsonify(error="Wrong format"), 400


@app_views.route('/users/<user_id>', methods=['POST'], strict_slashes=False)
def update_user():
    '''
    updates the user
    '''
    user = User.get(user_id)
    if user is None:
        return abort(404)
    if request.json():
        json = requests.get_json()
        if json.get('first_name'):
            new_user.first_name = json.get('first_name')
        if json.get('last_name'):
            new_user.first_name = json.get('last_name')
        db_session.commit()
        return jsonify(user.to_dict)
    else:
        return jsonify(error="Wrong format"), 400
