# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Stock(scrapy.Item):
#     # define the fields for your item here like:
#     ticker = scrapy.Field()
#     name = scrapy.Field()
#     intraday_price = scrapy.Field()
#     price_change = scrapy.Field()
#     percent_change = scrapy.Field()
#     volume = scrapy.Field()
#     avg_vol_3_month = scrapy.Field()
#     market_cap = scrapy.Field()
#     pe_ratio_ttm = scrapy.Field()
#     sector = scrapy.Field()

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
