#!/usr/bin/python3
'''
Improve the User class by adding the public instance method
def display_name(self): that displays the full name of an User instance:
'''

import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.my_user = User()

    def testUser(self):
        #check if email exists
        self.assertNotEqual(self.my_user.email, None)
        #check if first name exists
        self.assertNotEqual(self.my_user.first_name, None)
        #check if last name exists
        self.assertNotEqual(self.my_user.last_name, None)

if __name__ == '___main__':
    unittest.main()
