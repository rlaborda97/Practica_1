# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CasaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    summary = scrapy.Field()
    short_description = scrapy.Field()
    description = scrapy.Field()
    last_modified = scrapy.Field()
    distribution = scrapy.Field()
    general_characteristics = scrapy.Field()
