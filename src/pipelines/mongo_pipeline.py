import pymongo
from creds import MONGO_URI, MONGO_DATABASE, MONGO_COLLECTION
import logging

class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db, collection_name):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=MONGO_URI,
            mongo_db=MONGO_DATABASE,
            collection_name=MONGO_COLLECTION
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        logging.info(f"Connected to MongoDB: {self.mongo_uri}, Database: {self.mongo_db}")

    def close_spider(self, spider):
        self.client.close()
        logging.info("Closed MongoDB connection")

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
