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
    __password = None

    def __init__(self):
        self.email = 
        self.first_name =
        self.last_name =
        self.__password =
