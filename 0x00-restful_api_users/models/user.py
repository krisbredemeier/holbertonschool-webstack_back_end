#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, UniqueConstraint, DateTime
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

    '''
    stuff
    '''

    __tablename__ = 'users'
    email = Column(
        String(128),
        nullable=False
    )
    first_name = Column(
        String(128),
        nullable=False
    )
    last_name = Column(
        String(128),
        nullable=False
    )
    _password = Column(
        String(128),
        nullable=False
    )

    # Displays user with peramiters
    def display_name(self):
        '''
        stuff
        '''
        if
        self.email is None and \
            self.first_name is None and \
                self.last_name is None:
            return ''
        if self.first_name is None and self.last_name is None:
            return self.email
        elif self.last_name is None:
            return self.first_name
        elif self.first_name is None:
            return self.last_name
        else:
            return '{} {}'.format(self.first_name, self.last_name)

    # overrides str
    def __str__(self):
        '''
        stuff
        '''
        return '{} {} - {} - {}'.format(
            '[User]', self.id, self.email, self.display_name()
        )

    # creates getter to encrypt user password
    @property
    def password(self):
        '''
        stuff
        '''
        return self._password

    # setter for password
    @password.setter
    def password(self, value):
        '''
        stuff
        '''
        if value is None:
            self._password = None
        else:
            self._password = hashlib.md5(value.encode("utf8")).hexdigest()

    # validates that the value passed is the clear
    # version of the password of a User instance
    def is_valid_password(self, pwd):
        '''
        stuff
        '''
        if pwd is None or type(pwd) != str or self._password is None:
            return False
        if hashlib.md5(pwd.encode("utf8")).hexdigest() == self.password:
            return True
        else:
            return False

    # returns a serializable representation
    # (dictionary of integers and strings) of an User instance:
    def to_dict(self):
        '''
        stuff
        '''
        User = {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
        return User
