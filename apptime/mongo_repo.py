from pymongo import MongoClient

mongoclient = MongoClient(os.getenv('MONGOLAB_URI', 'mongodb://localhost:27017/apptime'))
db = mongoclient.get_default_database()
collection = db.usage