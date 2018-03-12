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
    pipeline = [
        {"$unwind": "$topics"},
        { "$group": {
            "_id": "$_id",
            "name": {"$student": "$name"},
            "count": {"$avg": "$topics.score"}}},
            # "each_score": {"$avg"["$topics.socre"]}
        {"$sort": {"count": -1}}
    ]
    pprint.pprint (list(mongo_collection.aggregate(pipeline)))
    # mongo_collection.command('aggregate', 'things', pipeline=pipeline, explain=True)
        # }])
    # return mongo_collection.find().sort({ "averageScore": pymongo.ASCENDING })
