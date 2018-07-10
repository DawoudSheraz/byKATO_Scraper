# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class BykatospiderPipeline(object):

    """
    Export scraped data as csv
    """

    def __init__(self):
        """
        Defining the CSVItemExporter
        """
        self.csv_exporter = CsvItemExporter(open('data.csv', 'wb'))
        self.csv_exporter.encoding = 'utf-8'
        self.csv_exporter.fields_to_export = [
            'title', 'label', 'link', 'image_title',
            'image_width', 'image_height', 'image_urls'
        ]
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        """
        Process and store the item.

        :param item: Item with extracted data
        :param spider: spider that extracted data
        :return: the item itself
        """
        self.csv_exporter.export_item(item)
        return item

    def spider_closed(self, spider):
        """
        Stop the exporting process.

        :param spider: Spider that extracted data
        """
        self.csv_exporter.finish_exporting()


class CustomImageNamePipeline(ImagesPipeline):

    """
    Pipeline to create images with their original name
    """

    def get_media_requests(self, item, info):
        """
        passing file name as meta information.

        :param item: item containing image url and name
        :param info: additional info
        :return: request with meta data as argument
        """
        return [Request(x, meta={'image_name': item["image_title"]})
                for x in item.get('image_urls', [])]

    def file_path(self, request, response=None, info=None):
        """
        Defining the path where files will be stored.

        :param request: the request containing the metadata
        :param response
        :param info
        :return: the intended path with custom file name
        """
        return 'full/%s.jpg' % request.meta['image_name']
