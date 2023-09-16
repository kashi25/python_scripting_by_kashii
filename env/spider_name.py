import scrapy


class SpiderNameSpider(scrapy.Spider):
    name = "spider_name"
    allowed_domains = ["cve.mitre.org"]
    start_urls = ["http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]

    def parse(self, response):
        pass
