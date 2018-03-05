#!/usr/bin/python3
from pymongo import MongoClient
Client = MongoClient('mongodb://127.0.0.1:27017')
db = Client.admin

def list_all(mongo_collection):
    lst_all = db.school.find()
    return (lst_all)
