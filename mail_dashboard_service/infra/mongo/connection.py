import pymongo
from config.environment import Settings

settings = Settings()

client = pymongo.MongoClient(settings.mongo.uri)


def get_db():
    return client[settings.mongo.db]

