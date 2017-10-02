#!/usr/bin/python3

'''
Now we will create a class
to manage the API authentication.
'''

from flask import request
from api.v1.auth.auth import Auth

class BasicAuth():

    def extract_base64_authorization_header(self, authorization_header):
        '''
         returns the Base64 part of the Authorization header
         for a Basic Authentication:
        '''
        if auth.authorization_header is None:
            return None
        if not str(auth.authorization_header):
            return None
        if Basic not in auth.authorization_header:
            return None
        else:
            return Basic
