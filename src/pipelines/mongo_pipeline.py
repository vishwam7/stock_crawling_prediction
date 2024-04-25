import pymongo
from scrapy.exceptions import DropItem
from creds import MONGO_URI, MONGO_DATABASE, MONGO_COLLECTION, HISTORY_COLLECTION
import logging

class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db, stocks_collection,history_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.stocks_collection = stocks_collection
        self.history_collection = history_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=MONGO_URI,
            mongo_db=MONGO_DATABASE,
            stocks_collection=MONGO_COLLECTION,
            history_collection=HISTORY_COLLECTION
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.stocks_col = self.db[self.stocks_collection]  # handle stocks collection
        self.history_col = self.db[self.history_collection]
        logging.info(f"Connected to MongoDB: {self.mongo_uri}, Database: {self.mongo_db}")

    def close_spider(self, spider):
        self.client.close()
        logging.info("Closed MongoDB connection")
        
    def process_item(self, item, spider):
        if item.__class__.__name__ == 'StockHistory':
            # Upsert operation to add historical data into an array within a single document per symbol
            update_result = self.history_col.update_one(
                {'symbol': item['symbol']},
                {'$push': {'history': dict(item)}},
                upsert=True
            )
            # Optionally handle the response of the update operation
            if update_result.upserted_id:
                return {'_id': update_result.upserted_id}
            return item
        elif item.__class__.__name__ == 'Stock':
            stock_data = dict(item)
            # Ensure we link history using history_id if available
            if 'history_id' in item:
                self.stocks_col.update_one({'symbol': item['symbol']}, {'$set': {'history_id': item['history_id']}})
            else:
                self.stocks_col.insert_one(stock_data)
            return item
        else:
            raise DropItem(f"Unknown item type: {type(item)}")

