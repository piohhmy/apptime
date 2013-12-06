import os
from pymongo import MongoClient
from bson.code import Code

mongoclient = MongoClient(os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017/apptime'))
db = mongoclient.get_default_database()
collection = db.usage

mapper = Code("function () {"
           "  emit(this.usage.name, this.usage.usage);"
           "}")

reducer = Code("function (key, values) {"
              "var total = 0;"
              "for (var i = 0; i < values.length; i++) {"
                   "total += values[i];"
                  "}"
              "return total;}")

def find_rec(username, category):
    records = collection.find({"username": username})
    ret_rec = []
    
    result = collection.map_reduce(mapper, reducer, "myresults", query={"username": username, "category": category})
    for doc in result.find():
        ret_rec.append({"name": doc["_id"], "weekly_usage": doc["value"]})
    return ret_rec

def insert(username, category, record):               
    entry = {"username": username, "category": category, "usage": record}
    return collection.insert(entry)
                
def empty():
    collection.remove()
