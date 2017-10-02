#!/usr/bin/python3

'''
Now we will create a class
to manage the API authentication.
'''

from flask import request
from api.v1.auth.auth import Auth
import base64


class BasicAuth():

    def extract_base64_authorization_header(self, authorization_header):
        '''
         returns the Base64 part of the Authorization header
         for a Basic Authentication:
        '''
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if "Basic" not in authorization_header:
            return None
        else:
            return authorization_header.split("Basic")[-1]


    def decode_base64_authorization_header(self, base64_authorization_header):
        '''
        returns the decoded value
        of a Base64 string base64_authorization_header:
        '''
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            if base64.b64decode(base64_authorization_header):
                return base64.b64decode(base64_authorization_header).decode('utf-8')
        except:
            return None


    def extract_user_credentials(self, decoded_base64_authorization_header):
        '''
        that returns the user email
        and password from the Base64 decoded value.
        '''
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        else:
            short_auth = decoded_base64_authorization_header
            return short_auth.split(":")[0], short_auth.split(":")[-1]
