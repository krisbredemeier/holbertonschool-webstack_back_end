#!/usr/bin/python3
'''
Write a Python script that provides some
stats about Nginx logs stored in MongoDB
'''
from pymongo import MongoClient





''' estiablish db connection and MongoClient '''
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    print("{} logs".format(logs))
    for method in methods:
        print("Methods: /n/t method {}: {} ".format(method))
