#!/usr/bin/python3
'''
Write a Python function that returns all students sorted by average score
'''
from pymongo import MongoClient
import pymongo

def top_students(mongo_collection):
    ''' sort students by score '''
    for score in mongo_collection.find({ "score": score }):
        ''' add the scores and dive by total for average '''

    return mongo_collection.find().sort({ "averageScorescore": pymongo.ASCENDING })
