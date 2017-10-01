#!/usr/bin/python3

'''
Now we will create a class
to manage the API authentication.
'''

from flask import request


class Auth():

    def require_auth(self, path, excluded_paths):
        '''
        hat returns False -
        path and excluded_paths will be used later, now,
        you don't need to take care of them
        '''
        if path is None or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None):
        '''
        that returns None -
        request will be the Flask request object
        '''
        if resquest is None or requset.header.get('Authorization') is None:
            return None
        else:
            return request.heades['Authorization']

    def current_user(self, request=None):
        '''
        that returns None -
        request will be the Flask request object
        '''
        return None
