#!/usr/bin/python3
from models.base_model import BaseModel

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
        if self.email and self.first_name and self.last_name == None:
            return ''
        if self.first_name and self.last_name == None:
            return self.email
        if self.last_name == None:
            return self.first_name
        if self.first_name == None:
            return self.last_name
        else:
            return (self.first_name, self.last_name)
