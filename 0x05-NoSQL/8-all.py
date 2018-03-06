#!/usr/bin/python3
from pymongo import MongoClient


def list_all(mongo_collection):
    # db = client.school
    # documents = db.school.find()
    # for document in documents:
    #     print (document)
    total_count = mongo_collection.count
    if total_count == 0:
        print("this collection is empty")
    else:
        return mongo_collection.find()
