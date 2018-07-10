# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter


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
