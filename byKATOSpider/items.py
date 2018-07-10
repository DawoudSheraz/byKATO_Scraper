# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class BykatoItem(scrapy.Item):

    """
    Item Data Model to store the extracted data
    """

    image_urls = Field()

    title = Field()
    link = Field()
    label = Field()
    image_title = Field()
    image_width = Field()
    image_height = Field()



