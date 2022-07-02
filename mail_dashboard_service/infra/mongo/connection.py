import pymongo
from config.environment import Settings

settings = Settings()

client = pymongo.MongoClient(settings.mongo.uri)

db = client[settings.mongo.db]
