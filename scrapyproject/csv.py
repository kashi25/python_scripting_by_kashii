import scrapy
import os
import csv

current_dir = os.path.dirname(__file__)
url= os.path.join(current_dir, 'source-EXPLOIT-DB.html')

class CsvSpider(scrapy.Spider):
    name = "csv"
    allowed_domains = ["cve.mitre.org"]
    start_urls= [f"file://{url}"]
    # start_urls = ["http://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]

    def parse(self, response):
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) > 100:
                table= child
                break
        count= 0
        csv_file = open('vulnerability.csv', 'w')
        writter = csv.writer(csv_file)
        writter.writerow(['exploit id', 'cve id'])
        for row in table.xpath('//tr'):
            if count > 100:
                break
            try:
                exploit_id= row.xpath('td//text()')[0].extract()
                cve_id= row.xpath('td//text()')[2].extract()
                writter.writerow([exploit_id,cve_id])
                count +=1
            except IndexError:
                pass
        csv_file.close()
