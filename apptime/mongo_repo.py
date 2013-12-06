import os
from pymongo import MongoClient

mongoclient = MongoClient(os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017/apptime'))
db = mongoclient.get_default_database()
collection = db.usage


def find_rec(username):
    records = collection.find({"username": username})
    ret_rec = []
    for record in records:
        ret_rec.append({"name": record["usage"]["name"], "weekly_usage": record["usage"]["usage"]})
        
    return ret_rec

def insert(username, record):	
    entry = {"username": username, "usage": record}
    return collection.insert(entry)
	
def empty():
    collection.remove()