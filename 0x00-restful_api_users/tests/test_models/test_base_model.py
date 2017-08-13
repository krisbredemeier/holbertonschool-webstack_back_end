#!/usr/bin/python3

'''
Does id, created_at and updated_at have a value when
you create a new instance of the BaseModel class?
Is id is unique?
etc...
'''

import unittest
from models.base_model import BaseModel, Base
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    '''
    Does id, created_at and updated_at have a value
    when you create a new instance of the BaseModel class?
    Is id is unique?
    '''

    def setUp(self):
        '''
        sets up instance for basemodel tests
        '''
        self.my_base_model = BaseModel()


    def test_id(self):
        '''
        check if id is unique
        '''
        bm = BaseModel()
        self.assertNotEqual(bm.id, self.my_base_model.id)
        self.assertTrue(type(self.my_base_model.id) == str)

    def test_created_at(self):
        '''
        test if created_at not empty
        '''
        self.assertNotEqual(self.my_base_model.created_at, None)
        # create_at is date time object

    def test_updated_at(self):
        '''
        test if updated_at is not empty
        '''
        self.assertNotEqual(self.my_base_model.updated_at, None)
        # updated_at is a datetime object

if __name__ == '___main__':
    unittest.main()
