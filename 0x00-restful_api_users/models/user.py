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
    a class User that defines the user model
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
        mprove the User class by adding the public instance method
        def display_name(self):
        that displays the full name of an User instance
        '''
        if (self.email is None and
            self.first_name is None and
                self.last_name is None):
                    return '{}'.format('')
        if self.first_name is None and self.last_name is None:
            return '{}'.format(self.email)
        if self.last_name is None:
            return '{}'.format(self.first_name)
        if self.first_name is None:
            return (self.last_name)
        else:
            return '{} {}'.format(self.first_name, self.last_name)

    # overrides str
    def __str__(self):
        '''
        Improve the class User by overriding the
        public instance method def __str__(self):
        to display a readable User instance
        '''
        return '{} {} - {} - {}'.format(
            '[User]', self.id, self.email, self.display_name()
        )

    # creates getter to encrypt user password
    @property
    def password(self):
        '''
        Improve the User class by adding public instance methods
        to access and assign a password to a User instance
        '''
        return self._password

    @password.setter
    def password(self, value):
        '''
        setter for password
        '''
        if value is None:
            self._password = None
        else:
            self._password = hashlib.md5(value.encode("utf8")).hexdigest()

    def is_valid_password(self, pwd):
        '''
        validates that the value passed is the clear
        version of the password of a User instance
        '''
        if pwd is None or type(pwd) != str or self._password is None:
            return False
        if hashlib.md5(pwd.encode("utf8")).hexdigest() == self.password:
            return True
        else:
            return False

    def to_dict(self):
        '''
        returns a serializable representation
        (dictionary of integers and strings) of an User instance:
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
