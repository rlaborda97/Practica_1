#from wsgiref import headers
#import scrapy
#from scrapy.item import Item, Field
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from ..items import CasaItem
import re

class habitacliaSpider(CrawlSpider):

    name = 'habitaclia'
    allowed_domains = ['www.habitaclia.com']
    start_urls = ['https://www.habitaclia.com/casas-la_nora-murcia.htm']

    rules = {
		# Para cada página.
        Rule(LinkExtractor(allow =(), restrict_xpaths = ('//li[@class="next"]/a'))),
        # Para cada item.
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h3[contains(@class,"list-item-title")]/a')),
							callback = 'parse_items', follow = True)
	}
    
    def parse_items(self, response):
        casa = CasaItem()
		#info de producto
        casa['name'] = response.xpath('normalize-space(//h1/text())').extract()
        casa['price'] = response.xpath('normalize-space(//div[@class="price"]/span/text())').extract()
        pattern = r"<.*?>"
        casa['summary'] = re.sub( "\s{2,}", "", "".join(re.sub(pattern, '', str(response.xpath('//article[contains(@id, "js-feature-container")]/ul[contains(@class, "feature-container")]/li').extract())))).replace("\\r\\n", "") #" ".join(re.sub(pattern, '', str(response.xpath('//article[contains(@id, "js-feature-container")]/ul[contains(@class, "feature-container")]/li').getall()))).split()
        casa['short_description'] = response.xpath('normalize-space(//h3/text())').extract()
        casa['description'] = response.xpath('normalize-space(//p[@class="detail-description"])').extract()
        casa['last_modified'] = response.xpath('normalize-space(//p[@class="time-tag"]/time)').extract()
        casa['distribution'] = response.xpath('//article[@class="has-aside"][2]/ul/li/text()').getall()
        casa['general_characteristics'] = response.xpath('//article[@class="has-aside"][3]/ul/li/text()').getall()
		#imagenes del producto
		#ml_item['image_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
		#ml_item['image_name'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
		##info de la tienda o vendedor
		#ml_item['vendedor_url'] = response.xpath('//*[contains(@class, "reputation-view-more")]/@href').extract()
		#ml_item['tipo_vendedor'] = response.xpath('normalize-space(//p[contains(@class, "power-seller")]/text())').extract()
		#ml_item['ventas_vendedor'] = response.xpath('normalize-space(//div[@class="feedback-title"]/text())').extract()
		#self.item_count += 1
		#if self.item_count > 5:
		#	raise CloseSpider('item_exceeded')
        yield casa

    # Para probar ejecutar: "scrapy crawl laliga".
    #def parse(self, response):
    #    rows = response.xpath("//section/div/section/article")
#
    #    for row in rows:
    #        name = row.xpath("./div/div/section[1]/h3/a/text()").get()
    #        url = response.xpath("//section/div/section/article/div/div/section[1]/h3/a/@href").get()
    #        price = row.xpath("./div/div/section[2]/article/span/text()").get()
    #        short_description = " ".join(" ".join(row.xpath("./div/div/section[1]/p[2]/text()").getall()).split())
    #        description = row.xpath("./div/div/section[1]/p[3]/text()").get()
    #        scrapy.Request(url,
    #                                 callback=self.get_price2)
    #       
    #        yield{
    #           "name": name,
    #           "price": price,
    #           "short_description": short_description,
    #           "description": description,
    #           "price2": self.price2,
    #        }
    #
    #def get_price2(self, response):
    #        self.price2 = "2"#response.xpath("//section[3]/div/div/div/span/text()").get()
    #        yield self.price2
