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

    def testuser(self):
        '''
        test combiantion of user
        '''

        self.assertTrue(
            (self.my_user.last_name, None) and (self.my_user.first_name, None),
            (type(self.my_user.email) == str)
        )
        self.assertTrue(
            (self.my_user.last_name, None),
            (type(self.my_user.first_name) == str)
        )
        self.assertTrue(
            (self.my_user.first_name, None),
            (type(self.my_user.last_name) == str)
        )


    # tests for the user class
    def testUseEmail(self):
        '''
        test all possible cases for user error in email
        '''
        # check if email exists
        self.assertNotEqual(self.my_user.email, None)
        self.assertEqual(self.my_user.email, 'test@test.test')
        # make sure email is String
        self.assertTrue(type(self.my_user.email) == str)

    def testUserFirst(self):
        '''
        test all possible cases for user error in first name
        '''
        # check if first name exists
        self.assertNotEqual(self.my_user.first_name, None)
        # make sure first name is String
        self.assertTrue(type(self.my_user.first_name) == str)

    def testUserLast(self):
        '''
        test all possible cases for user error in last name
        '''
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

    def testStr(self):
        '''
        Test the overriding the pulblic instance method
        '''
        self.assertNotEqual(str(self.my_user), "")
        # test the format of the return
        format = '{} {} - {} - {}'.format(
            '[User]',
            self.my_user.id,
            self.my_user.email,
            self.my_user.display_name()
        )
        self.assertNotEqual(str(self.my_user), "")

    def testDict(self):
        '''
        test to make sure to_dic returns a serializable representation
        of a User instance
        '''
        dict = self.my_user.to_dict()
        self.assertTrue(type(dict['id']) == str)
        self.assertTrue(type(dict['email']) == str)
        self.assertTrue(type(dict['first_name']) == str)
        self.assertTrue(type(dict['last_name']) == str)
        self.assertIsNotNone(dict)

if __name__ == '___main__':
    unittest.main()
