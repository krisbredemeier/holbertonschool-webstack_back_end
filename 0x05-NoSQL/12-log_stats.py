#!/usr/bin/python3
'''
Write a Python script that provides some
stats about Nginx logs stored in MongoDB
'''
from pymongo import MongoClient


def count(mongo_collection):
    ''' count collection'''
    return mongo_collection.count()


def count_by_method(mongo_collection, method):
    ''' count methods '''
    return mongo_collection.count({"method": method})


''' estiablish db connection and MongoClient '''
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    ''' database is logs and collection is nginx '''
    nginx = client.logs.nginx
    ''' count nginx logs '''
    print("{} logs".format(count(nginx)))
    ''' log methods '''
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print("\t method {}: {}".format(
            method,
            count_by_method(nginx, method)
            )
        )
    print("{} status check".format(count(nginx)))
