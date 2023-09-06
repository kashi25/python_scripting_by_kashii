import scrapy


class NameOfSpiderIsFirstSpider(scrapy.Spider):
    name = "name_of_spider_is_first"
    allowed_domains = ["any_domain_name.org"]
    start_urls = ["https://any_domain_name.org"]

    def parse(self, response):
        pass
