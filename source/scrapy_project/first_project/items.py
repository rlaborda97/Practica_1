import scrapy

# Definición de la clase "CasaItem" con los campos en los cuales se almacenará la información extraida.
class CasaItem(scrapy.Item):
    # Información de las viviendas.
    name = scrapy.Field()
    price = scrapy.Field()
    summary = scrapy.Field()
    short_description = scrapy.Field()
    description = scrapy.Field()
    last_modified = scrapy.Field()
    distribution = scrapy.Field()
    general_characteristics = scrapy.Field()
    # Información de las imágenes.
    image_urls = scrapy.Field()
    saved_path = scrapy.Field()
    image_names = scrapy.Field()
    folder1 = scrapy.Field()
