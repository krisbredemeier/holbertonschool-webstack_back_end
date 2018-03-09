#!/usr/bin/python3
'''
Write a Python function that returns the list of school having a specific topic
'''
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    ''' find and return school based on topic '''
    total_count = mongo_collection.count({"topic": topic})
    if total_count == 0:
        # print("this collection is empty")
        return []
    else:
        return mongo_collection.find({"topics": {"$eq": topic}})
