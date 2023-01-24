from pymongo import MongoClient
import cfg


client = MongoClient(cfg.mongo_client_key)

db = client[cfg.database_name]
collection = db[cfg.collection_name]

db2 = client[cfg.database_name2]
collection2 = db2[cfg.collection_name2]

