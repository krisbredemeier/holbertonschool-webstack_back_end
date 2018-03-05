#!/usr/bin/python3
# from pymongo import MongoClient

conMongo = MongoClient(connect, 27017)
listOfDBs = conMongo.database_names()

def list_all(mongo_collection):
    for in in listOfDBs:
        db = conMongo[i]
        print db
        pring db.colection_names():
    conMongo.disconnect()
