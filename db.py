from pymongo import MongoClient
import cfg


client = MongoClient(cfg.mongo_client_key)
db = client[cfg.database_name]
collection = db[cfg.collection_name]

