#!/usr/bin/python3
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')


def list_all(mongo_collection):
    db = client.school
    documents = db.school.find()
    for document in documents:
        print (document)
