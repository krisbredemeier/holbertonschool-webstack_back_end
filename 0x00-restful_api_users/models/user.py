#!/usr/bin/python3
from models.base_model import BaseModel
import hashlib

'''
Write a class User that defines the user model:

Inherits from BaseModel
Public class attributes:
email initialized to None
first_name initialized to None
last_name initialized to None
Protected class attributes:
_password initialized to None
'''

class User(BaseModel):

    email = None
    first_name = None
    last_name = None
    _password = None

    def display_name(self):
        if self.email == None and self.first_name == None and self.last_name == None:
            return ''
        if self.first_name == None and self.last_name == None:
            return self.email
        if self.last_name == None:
            return self.first_name
        if self.first_name == None:
            return self.last_name
        else:
            return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{} {} - {} - {}'.format('[User]', self.id, self.email, self.display_name())

    # creates getter to encrypt user password
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if value == None:
            self._password = None
        else:
            self._password = hashlib.md5(value.encode("utf8")).hexdigest()

    # validates that the value passed is the clear
    # version of the password of a User instance
    def is_valid_password(self, pwd):
        if pwd == None or type(pwd) != str or self._password == None:
            return False
        if hashlib.md5(pwd.encode("utf8")).hexdigest() == self.password:
            return True
        else:
            return False
