from __future__ import absolute_import
import scrapy
from scrapy import Selector
import re
from scrapy.shell import inspect_response
from scrapy_splash import SplashRequest
from src.items import Stock, StockHistory
from creds import MONGO_URI, MONGO_DATABASE, MONGO_COLLECTION, HISTORY_COLLECTION
import pymongo


class HistorySpider(scrapy.Spider):
    name = 'stock_history'
    allowed_domains = ['finance.yahoo.com']	

    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DATABASE]

    def start_requests(self):
        stocks = self.db['stocks'].find({}, {'symbol': 1})
        for stock in stocks:
            symbol = stock['symbol']
            history_url = f'https://finance.yahoo.com/quote/{symbol}/history?period1=1556037632&period2=1713889315&frequency=1mo'
            yield SplashRequest(history_url, self.parse_history, args={'wait': 0.5}, meta={'symbol': symbol})

    def parse_history(self, response):
        symbol = response.meta['symbol']
        rows = response.xpath('//table[contains(@class, "table")]/tbody/tr')
        for row in rows:
            item = StockHistory(
                symbol=symbol,
                date=row.xpath('./td[1]/text()').get(),
                open=row.xpath('./td[2]/text()').get(),
                high=row.xpath('./td[3]/text()').get(),
                low=row.xpath('./td[4]/text()').get(),
                close=row.xpath('./td[5]/text()').get(),
                adj_close=row.xpath('./td[6]/text()').get(),
                volume=row.xpath('./td[7]/text()').get(),
            )
            yield item
