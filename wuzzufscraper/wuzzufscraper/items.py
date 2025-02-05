# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WuzzufscraperItem(scrapy.Item):

    name = scrapy.Field()
    company_name = scrapy.Field()
    type = scrapy.Field()
    mode = scrapy.Field()
    city = scrapy.Field()
    governate = scrapy.Field()
    country = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()