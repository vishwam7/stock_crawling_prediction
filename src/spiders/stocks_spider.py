from __future__ import absolute_import
import scrapy
from src.items import Stock
from scrapy import Selector
import re
from scrapy.shell import inspect_response
from scrapy_splash import SplashRequest

class StocksSpider(scrapy.Spider):
  name = 'stocks'
  start_urls = [
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_basic-materials/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_communication-services/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_consumer-cyclical/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_consumer-defensive/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_energy/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_financial-services/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_healthcare/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_industrials/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_real-estate/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_technology/?offset=0&count=100',
    'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_utilities/?offset=0&count=100',
  ]

  def convert_to_number(self, value):
    multiplier = 1
    if 'B' in value:
        multiplier = 1e9
    elif 'M' in value:
        multiplier = 1e6
    elif 'K' in value:
        multiplier = 1e3
    elif 'T' in value:
        multiplier = 1e12

    # Remove any non-numeric characters except '.'
    numeric_value = ''.join(filter(lambda x: x.isdigit() or x == '.', value))
    return float(numeric_value) * multiplier if numeric_value else None
  
  def extract_sector_name(self, url):
    # Extract the sector name from the URL using regular expression
    match = re.search(r'/sectors/([^/?]*)', url)
    if match:
        # Replace hyphens with spaces and capitalize each word
        return match.group(1).replace('-', ' ').title()
    return None

  def start_requests(self):
        for url in self.start_urls:
            print('I am waiting for 0.5 secs')
            sector_name = self.extract_sector_name(url)
            yield SplashRequest(url, self.parse, args={'wait': 0.5}, meta={'sector_name': sector_name})

  def extract_sector_name(self, url):
    match = re.search(r'sec-ind_sec-largest-equities_([^/?]*)', url)
    return match.group(1).replace('-', ' ').title() if match else None
  
  def parse(self, response):
    sector_name = self.extract_sector_name(response.url)

    for row in response.xpath('//table[contains(@class, "W(100%)")]/tbody/tr'):
        item = Stock()
        item['sector_name'] = sector_name
        item['symbol'] = row.xpath('.//td[1]/a/text()').get()
        item['company_name'] = row.xpath('.//td[2]/text()').get()
        item['last_price'] = row.xpath('.//td[3]/fin-streamer/@value').get()
        item['change'] = row.xpath('.//td[4]/fin-streamer/span/text()').get()
        item['percent_change'] = row.xpath('.//td[5]/fin-streamer/span/text()').get()
        item['volume'] = row.xpath('.//td[6]/fin-streamer/@value').get()
        item['avg_vol_3m'] = row.xpath('.//td[7]/text()').get()
        item['market_cap'] = row.xpath('.//td[8]/fin-streamer/@value').get()
        item['pe_ratio_ttm'] = row.xpath('.//td[9]/text()').get()

        yield item