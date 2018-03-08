#!/usr/bin/python3
'''
Write a Python function that returns all students sorted by average score
'''
from pymongo import MongoClient
from bson.son import SON
import pymongo
import pprint

def top_students(mongo_collection):
    ''' sort students by score '''
    # return mongo_collection.aggregate([{
        pipeling = [
            {"$unwind": "$topics"},
            { "$group": {
                "_id": "$name",
                "each_score": {"$avg"["$topics.socre"]}
                }
        ]

        mongo_collection('aggregate', pipeline=pipeline, explain=True)
        # }])
    # return mongo_collection.find().sort({ "averageScore": pymongo.ASCENDING })
