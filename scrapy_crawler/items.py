# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ScrapyCrawlerMotel(scrapy.Item):
    title=scrapy.Field()
    price=scrapy.Field()
    area=scrapy.Field()
    address=scrapy.Field()
    description=scrapy.Field()
    url=scrapy.Field()
    telephone=scrapy.Field()