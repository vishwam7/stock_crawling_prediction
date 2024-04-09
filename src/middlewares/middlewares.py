from scrapy import signals

class StocksScraperSpiderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class StocksScraperDownloaderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # This method is called for each request that goes through the downloader middleware.
        return None

    def process_response(self, request, response, spider):
        # This method is called with the response returned from the downloader.
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or process_request() raises an exception.
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
