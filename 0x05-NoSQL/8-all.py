#!/usr/bin/python3
from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')


def list_all(mongo_collection):
    db = client.school
    lst_all = db.school.find({"name": "Holberton school"})
    print (lst_all)
