import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")


class MongoDB:
    def __init__(self, database_name):
        self.uri = MONGO_URI
        self.database_name = database_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri, server_api=ServerApi("1"))
            self.db = self.client[self.database_name]
            print("You successfully connected to MongoDB!")
            return True
        except Exception as e:
            print(e)
            return False

    def insert_one(self, collection_name, item):
        if self.client is None:
            print("Not connected to MongoDB. Call connect() method first.")
            return

        try:
            collection = self.db[collection_name]
            result = collection.insert_one(item)
            print(f"Inserted item with ID: {result.inserted_id}")
        except Exception as e:
            print("Error inserting item:", e)

    def get_counts(self, collection_name):
        if self.client is None:
            print("Not connected to MongoDB. Call connect() method first.")
            return

        try:
            collection = self.db[collection_name]
            return collection.count_documents({})
        except Exception as e:
            print("Error getting counts:", e)

    def delete_all(self, collection_name):
        if self.client is None:
            print("Not connected to MongoDB. Call connect() method first.")
            return

        try:
            collection = self.db[collection_name]
            result = collection.delete_many({})
            print(f"Deleted {result.deleted_count} items")
        except Exception as e:
            print("Error deleting items:", e)
