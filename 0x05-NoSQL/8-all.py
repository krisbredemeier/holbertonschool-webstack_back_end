#!/usr/bin/python3
''' Write a Python function that lists all documents in a collection '''
from pymongo import MongoClient


def list_all(mongo_collection):
    ''' count collection to see if it's empty '''
    total_count = mongo_collection.count()
    if total_count == 0:
        print("this collection is empty")
        return []
    else:
        return mongo_collection.find()
