from pymongo import MongoClient

def list_all(mongo_collection)
if __name__ == '__main__':
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.localhost
    collection = db['school']
    cursor = collection.find({})
    for document in cursor:
          print(document)
