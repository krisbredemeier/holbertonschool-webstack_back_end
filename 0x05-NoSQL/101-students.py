#!/usr/bin/python3
'''
Write a Python function that returns all students sorted by average score
'''
from pymongo import MongoClient
import pymongo

def top_students(mongo_collection):
    ''' sort students by score '''
    return mongo_collection.find().sort({ "score": pymongo.ASCENDING })
