from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME

class MongoDBHandler:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def save_metadata(self, data):
        self.collection.insert_one(data)
        print(f"Stored {data['file_name']} metadata in MongoDB.")

    def update_with_summary_and_keywords(self, file_name, summary, keywords):
        self.collection.update_one(
            {"file_name": file_name},
            {"$set": {"summary": summary, "keywords": keywords}},
            upsert=True
        )
