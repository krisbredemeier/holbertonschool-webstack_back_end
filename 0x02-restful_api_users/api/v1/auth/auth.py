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
        return False

    def authorization_header(self, request=None):
        '''
        that returns None -
        request will be the Flask request object
        '''
        return None

    def current_user(self, request=None):
        '''
        that returns None -
        request will be the Flask request object
        '''
        return None
