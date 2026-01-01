from pymongo import MongoClient
from app.config import config

client = MongoClient(config.mongo_uri)
db = client[config.MONGO_DB]
collection = db.data
