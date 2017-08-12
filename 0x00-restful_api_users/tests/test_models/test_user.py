#!/usr/bin/python3
'''
Improve the User class by adding the public instance method
def display_name(self): that displays the full name of an User instance:
'''

import unittest
from models.base_model import BaseModel
from models.user import User
import hashlib


class TestUser(unittest.TestCase):
    '''
    stuff
    '''

    # sets up instance of my_user
    def setUp(self):
        '''
        stuff
        '''
        self.my_user = User()
        self.my_user.email = 'test@test.test'
        self.my_user.first_name = 'first'
        self.my_user.last_name = 'last'
        self.my_user.password = 'abc'

    # tests for the user class
    def testUser(self):
        '''
        stuff
        '''
        # check if email exists
        self.assertNotEqual(self.my_user.email, None)
        self.assertEqual(self.my_user.email, 'test@test.test')
        # make sure email is String
        self.assertTrue(type(self.my_user.email) == str)
        # check if first name exists
        self.assertNotEqual(self.my_user.first_name, None)
        # make sure first name is String
        self.assertTrue(type(self.my_user.first_name) == str)
        # check if last name exists
        self.assertNotEqual(self.my_user.last_name, None)
        # make sure email is String
        self.assertTrue(type(self.my_user.last_name) == str)

    # tests for password method
    def testPwd(self):
        '''
        stuff
        '''
        # check if password exists
        self.assertNotEqual(self.my_user.password, None)
        # make sure email is String
        self.assertTrue(type(self.my_user.password) == str)
        # check to make sure hash is same as password
        self.assertEqual(
            self.my_user.password,
            hashlib.md5('abc'.encode("utf8")).hexdigest()
        )


if __name__ == '___main__':
    unittest.main()
