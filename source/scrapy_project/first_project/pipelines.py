from itemadapter import ItemAdapter
import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy import Spider
import csv

# Pipeline para almacenar los datos en un fichero csv.
class HousesPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        # Ruta en la que se almacenarán los datos.
        file = open('../../../dataset/%s_houses.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        # Datos a almacenar en el csv.
        self.exporter.fields_to_export = ["name", "price", "summary", "short_description", "description", "last_modified", "distribution", "general_characteristics", "saved_path"]
        self.exporter.start_exporting()
     
    
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

# Pipeline para almacenar las imágenes por carpetas.
class HousesImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        return [Request("https:" + x, meta={'image_name': y, 'folder1': item["folder1"]})
                for x, y in zip(item.get('image_urls', []), item.get('image_names', []))]

    def file_path(self, request, response=None, info=None):
        return '{}/{}'.format(request.meta['folder1'], request.meta['image_name'])