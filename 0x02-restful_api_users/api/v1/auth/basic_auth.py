#!/usr/bin/python3

'''
Now we will create a class
to manage the API authentication.
'''

from flask import request
from api.v1.auth.auth import Auth
import base64
from models import db_session
from models import User


class BasicAuth(Auth):
    '''
    documentation
    '''

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
            return authorization_header.split("Basic ")[-1]

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
            b64 = base64.b64decode
            if b64(base64_authorization_header):
                return b64(base64_authorization_header).decode('utf-8')
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

    def user_object_from_credentials(self, user_email, user_pwd):
        '''
        returns the User instance based on his email and password.
        '''
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_email) != str:
            return None
        user = db_session.query(User).filter_by(email = user_email).first()
        if user is None:
            return None
        if not user.is_valid_password(user_pwd):
            return None
        else:
            return user

    def current_user(self, request=None):
        '''
        overloads Auth and retrieves the User instance for a request:
        '''
        self.authorization_header(request)
        return request
        self.extract_base64_authorization_header(authorization_header)
        return authorization_header
        self.decode_base64_authorization_header(base64_authorization_header)
        return base64_authorization_header
        self.extract_user_credentials(decoded_base64_authorization_header)
        return decoded_base64_authorization_header
        self.user_object_from_credentials(user_email, user_pwd)
        return user_email, user_pwd
