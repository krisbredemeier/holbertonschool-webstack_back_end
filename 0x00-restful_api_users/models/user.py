#!/usr/bin/python3
from models.base_model import BaseModel
import hashlib
import datetime


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

# defines user class
class User(BaseModel):

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    _password = Column(String(128), nullable=False)

    # Displays user with peramiters
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

    # overrides str
    def __str__(self):
        return '{} {} - {} - {}'.format('[User]', self.id, self.email, self.display_name())

    # creates getter to encrypt user password
    @property
    def password(self):
        return self._password

    # setter for password
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

    # returns a serializable representation
    # (dictionary of integers and strings) of an User instance:
    def to_dict(self):
        User = {'id':self.id, 'email':self.email, 'first_name':self.first_name, 'last_name':self.last_name, 'created_at':self.created_at, 'updated_at':self.updated_at}
        return User
