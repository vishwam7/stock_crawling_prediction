from __future__ import absolute_import
import scrapy
from src.items import Stock
from scrapy import Selector
import re
from scrapy.shell import inspect_response

class StocksSpider(scrapy.Spider):
  name = 'stocks'
  start_urls = [
    'https://finance.yahoo.com/sectors/basic-materials/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/communication-services/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/consumer-cyclical/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/consumer-defensive/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/energy/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/financial-services/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/healthcare/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/industrials/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/real-estate/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/technology/?offset=0&count=100',
    'https://finance.yahoo.com/sectors/utilities/?offset=0&count=100',
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
  
  def parse(self, response):
    sector_name = self.extract_sector_name(response.url)
    for row in response.xpath('//table[contains(@class, "expandable-table")]/tbody/tr'):
        item = Stock()
        # Extract the stock symbol and company name from the link's text
        item['symbol'] = row.xpath('.//td[1]//span[contains(@class, "symbol")]/text()').get()
        
        # Extracting the company name
        item['company_name'] = row.xpath('.//td[1]//span[contains(@class, "longName")]/text()').get()

        # Extracting and converting the last_price
        last_price = row.xpath('.//td[2]/span/text()').get()
        item['last_price'] = self.convert_to_number(last_price) if last_price else None
        print("Inserting last_price:", item['last_price'])

        # Extracting and converting the target_price (1Y Target Est.)
        target_price = row.xpath('.//td[3]/span/text()').get()
        item['target_price'] = self.convert_to_number(target_price) if target_price else None
        print("Inserting target_price:", item['target_price'])


        market_weight = row.xpath('.//td[4]/span/text()').get()
        if market_weight:
            market_weight = market_weight.replace('%', '').strip()
            item['market_weight'] = float(market_weight) if market_weight else None
        print("Inserting market_weight:", item['market_weight'])
        
        
        # Extracting data from <fin-streamer> elements; this might require JavaScript rendering
        # If the data isn't loaded properly, you might need to use Scrapy-Splash or Selenium
        market_cap = row.xpath('.//td[5]/span/fin-streamer/@data-value').get()
        if market_cap:
           item['market_cap'] = self.convert_to_number(market_cap) if market_cap else None
        print("Inserting market_cap:", item['market_cap'])  
        # Extracting the Day Change Percentage
        # Note: The day change percentage is contained within a fin-streamer element, which might be dynamically loaded.
        # If the values are not being extracted, it might be due to the page's dynamic content loading.
  
        day_change_percentage = row.xpath('.//td[6]//fin-streamer[contains(@data-field, "regMarketChangePercent")]/@data-value').get()
        if day_change_percentage:
            item['day_change_percentage'] = day_change_percentage.strip() + '%'  # Adding '%' back if needed
        else:
            item['day_change_percentage'] = None
        # Extracting the YTD Return
        print("Inserting day_change_percentage:", item['day_change_percentage'])  
        
        
        ytd_return = row.xpath('.//td[7]//fin-streamer[contains(@data-field, "ytdReturn")]/span/text()').get()
        # The extracted value could include '+' or '-', so it's directly usable as a string.
        # If you need to convert it to a numerical type, ensure to handle the conversion appropriately.
        if ytd_return:
            item['ytd_return'] = ytd_return.strip()
        else:
            item['ytd_return'] = None  # or some default value or handling
        print("Inserting ytd_return:", item['ytd_return']) 
        
        
        # Analyst rating might require some logic if there are different classes for Buy/Hold etc.
        buy_hold_recommendation = row.xpath('.//td[8]//div[@data-testid="table-cell-rating"]/text()').get()
        item['buy_hold_recommendation'] = buy_hold_recommendation.strip() if buy_hold_recommendation else None
        print("Inserting buy_hold_recommendation:", item['buy_hold_recommendation'])

        # These items need to be filled with your own logic or adjusted according to the page structure
        item['sector_name'] = sector_name  # Example static assignment

        yield item