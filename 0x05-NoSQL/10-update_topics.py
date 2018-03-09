#!/usr/bin/python3
'''
Write a Python function that changes all topics
of a school document based on the name
'''
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    ''' name of school to update with update_topics'''
    mongo_collection.update({"name": name},
                            {"$set": {"topics": topics}})
