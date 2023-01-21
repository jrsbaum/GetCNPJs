from pymongo import MongoClient
from cfg import mongo_client_key


client = MongoClient(mongo_client_key)
db = client.BigDataCorpProcesses
Processes = db.Processes

