#!/usr/bin/python3
'''
Improve the User class by adding the public instance method
def display_name(self): that displays the full name of an User instance:
'''

import unittest
from models.base_model import BaseModel
from models.user import User


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

    # tests for the user class
    def testUser(self):
        '''
        stuff
        '''
        # check if email exists
        self.assertNotEqual(self.my_user.email, None)
        # check if first name exists
        self.assertNotEqual(self.my_user.first_name, None)
        # check if last name exists
        self.assertNotEqual(self.my_user.last_name, None)
        # check if password exists
        self.assertNotEqual(self.my_user._password, None)

    # tests for password method
    def testPwd(self):
        '''
        stuff
        '''
        # check if pwd is equal to self.password
        self.assertNotEqual(self.my_user._password, self.password)

if __name__ == '___main__':
    unittest.main()
