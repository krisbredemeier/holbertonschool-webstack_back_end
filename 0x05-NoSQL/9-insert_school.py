#!/usr/bin/python3
'''
Write a Python function that inserts a
new document in a collection based on kwargs
'''
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    ''' return new id'''
    return mongo_collection.insert(kwargs)
    # return mongo_collection.new_school_id
