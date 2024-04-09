# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Stock(scrapy.Item):
    symbol = scrapy.Field()
    company_name = scrapy.Field()
    last_price = scrapy.Field()
    target_price = scrapy.Field()
    market_cap = scrapy.Field()
    day_change_percentage = scrapy.Field()
    ytd_return = scrapy.Field()
    buy_hold_recommendation = scrapy.Field()
    sector_name = scrapy.Field()
    industry_name = scrapy.Field()
    market_weight = scrapy.Field()
    sector_day_return = scrapy.Field()
    sector_ytd_return = scrapy.Field()
    industry_day_return = scrapy.Field()
    industry_ytd_return = scrapy.Field()

    # symbol = scrapy.Field()  # Stock symbol, e.g., "AMZN"
    company_name = scrapy.Field()  # Full company name, e.g., "Amazon.com, Inc."
    last_price = scrapy.Field()  # Price (Intraday)
    change = scrapy.Field()  # Change in price
    percent_change = scrapy.Field()  # Percentage change in price
    volume = scrapy.Field()  # Volume
    avg_vol_3m = scrapy.Field()  # Average Volume (3 months)
    market_cap = scrapy.Field()  # Market Cap
    pe_ratio_ttm = scrapy.Field()  # PE Ratio (TTM)
    # The 52-week range is typically represented visually on websites and might not be directly scrapeable as text. You may need to handle this differently or exclude it if not essential.
    week_52_range = scrapy.Field() 
