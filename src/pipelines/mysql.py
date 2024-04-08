from __future__ import absolute_import
from mysql import connector
from creds import Creds

# class MySQLPipeline(object):
#   def __init__(self):
#     self.host = Creds.host
#     self.user = Creds.user
#     self.passwd = Creds.passwd

#   def open_spider(self, spider):
#     print('setting up database...')
#     self.db = connector.connect(host=self.host, user=self.user, passwd=self.passwd)
#     print('setting up cursor...')
#     self.cursor = self.db.cursor()
#     self.cursor.execute('USE investments')

#   def close_spider(self, spider):
#     self.db.commit()
#     print('closing cursor...')
#     self.cursor.close()
#     print('closing database...')
#     self.db.close()

#   def process_item(self, item, spider):
#     sql = "INSERT INTO stocks (ticker, name, intraday_price, price_change, percent_change, volume, avg_vol_3_month, market_cap, pe_ratio_ttm, sector) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     val = (item['ticker'], item['name'], item['intraday_price'], item['price_change'], item['percent_change'], item['volume'], item['avg_vol_3_month'], item['market_cap'], item['pe_ratio_ttm'], item['sector'])
#     self.cursor.execute(sql, val)
    
#     return item
class MySQLPipeline(object):
    def __init__(self):
        self.host = Creds.host
        self.user = Creds.user
        self.passwd = Creds.passwd

    def open_spider(self, spider):
        print('setting up database...')
        self.db = connector.connect(host=self.host, user=self.user, passwd=self.passwd)
        print('setting up cursor...')
        self.cursor = self.db.cursor()
        self.cursor.execute('USE investments')

    def close_spider(self, spider):
        self.db.commit()
        print('closing cursor...')
        self.cursor.close()
        print('closing database...')
        self.db.close()

    def process_item(self, item, spider):
      sql = ("INSERT INTO stocks (symbol, company_name, last_price, target_price, market_cap, "
       "day_change_percentage, ytd_return, buy_hold_recommendation, sector_name) "
       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        
      # Make sure the order of these values matches the order in your SQL statement
      val = (
          item.get('symbol'),
          item.get('company_name'),
          item.get('last_price'),
          item.get('target_price'),
          item.get('market_cap'),
          item.get('day_change_percentage'),
          item.get('ytd_return'),
          item.get('buy_hold_recommendation'),
          item.get('sector_name'),
      )

      self.cursor.execute(sql, val)
      return item