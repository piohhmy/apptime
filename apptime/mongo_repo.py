import os
from pymongo import MongoClient

mongoclient = MongoClient(os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017/apptime'))
db = mongoclient.get_default_database()
collection = db.usage


def find_rec(id):
	collection.find_one({"_id": id})

def insert(username, record):	
	entry = {"username": username, "usage": record}
	return collection.insert(entry)
	
def empty():
	collection.remove()