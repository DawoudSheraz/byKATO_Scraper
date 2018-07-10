import json
import scrapy
from scrapy.spiders import CrawlSpider
from byKATOSpider.items import BykatoItem


class ByKatoSpider(CrawlSpider):

    name = "byKato"

    base_url = 'http://bykato.com/products/?alttemplate=AjaxOverview&page=%s'
    count = 1
    start_urls = [
        base_url % count,
    ]

    def parse(self, response):
        """
        Parse requests and generates new till end of page is met.

        :param response: Fetched Page
        :return: New Request for additional data
        """

        out_data = json.loads(response.body)
        out_data = out_data['data']

        # If no more data is loaded
        if out_data is None:
            return

        # If there is data, get each entry
        for each in out_data['stories']:
            bykato_item = BykatoItem()

            bykato_item['title'] = self.get_json_item(each, 'title')
            bykato_item['label'] = self.get_json_item(each, 'label')
            bykato_item['link'] = self.get_json_item(each, 'link')

            bykato_item['image_title'] = self.get_json_item(each['images']
                                                            , 'title')
            bykato_item['image_width'] = self.get_json_item(each['images']
                                                            , 'width')
            bykato_item['image_height'] = self.get_json_item(each['images']
                                                             , 'height')

            bykato_item['image_urls'] = self.get_image_url(each)

            yield bykato_item

        # Creating new request for further data
        self.count += 1

        yield scrapy.Request(self.base_url % self.count)

    def get_image_url(self, json_object):
        """
        Create the url for the image
        :param json_object: containing the data
        :return: list containing image url
        """
        return ["http://bykato.com%s" % json_object['images']['normal']]

    def get_json_item(self, json_object, key):
        """
        Returns json item with mentioned key

        :param json_object: Data object
        :param key: Key through which entry will be searched
        :return: Required Data, empty if key missing
        """
        value = ""
        try:
            value = json_object[key]
        except KeyError, TypeError:
            pass
        return value






