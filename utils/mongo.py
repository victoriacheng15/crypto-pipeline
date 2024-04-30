import os, logging
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("MONGO_DB")


class MongoDB:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.uri = MONGO_URI
        self.database_name = DB_NAME
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri, server_api=ServerApi("1"))
            self.db = self.client[self.database_name]
            self.logger.info("You successfully connected to MongoDB!")
            return True
        except Exception as e:
            self.logger.error(f"Failed to connect to the MongoDB. Error: {e}")
            return False

    def close(self):
        if self.client:
            self.client.close()
            self.logger.info("The MongoDB connection has been closed.")

    def insert_one(self, collection_name, item):
        if self.client is None:
            self.logger.error("Not connected to MongoDB. Call connect() method first.")
            return

        try:
            collection = self.db[collection_name]
            result = collection.insert_one(item)
            self.logger.info(f"Inserted item with ID: {result.inserted_id}")
        except Exception as e:
            self.logger.error(f"Error inserting item: {e}")

    def get_counts(self, collection_name):
        if self.client is None:
            self.logger.error("Not connected to MongoDB. Call connect() method first.")
            return

        try:
            collection = self.db[collection_name]
            return collection.count_documents({})
        except Exception as e:
            self.logger.error(f"Error getting counts: {e}")

    def get_all_documents(self, collection_name):
        if self.client is None:
            self.logger.error("Not connected to MongoDB. Call connect() method first.")
            return
        try:
            collection = self.db[collection_name]
            return tuple([doc for doc in collection.find({})])
        except Exception as e:
            self.logger.error(f"Error getting all documents: {e}")

    def delete_all(self, collection_name):
        if self.client is None:
            self.logger.error("Not connected to MongoDB. Call connect() method first.")
            return

        try:
            collection = self.db[collection_name]
            result = collection.delete_many({})
            self.logger.info(f"Deleted {result.deleted_count} items")
        except Exception as e:
            self.logger.error(f"Error deleting items: {e}")
