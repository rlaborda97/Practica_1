import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from ..items import CasaItem
import re
import uuid

class habitacliaSpider(CrawlSpider):

    name = 'habitaclia'
    allowed_domains = ['www.habitaclia.com']
    start_urls = ['https://www.habitaclia.com/casas-la_nora-murcia.htm']

    rules = {
		# Regla de navegación para ir por cada página del listado.
        Rule(LinkExtractor(allow =(), restrict_xpaths = ('//li[@class="next"]/a'))),
        # Regla de navegación para ir por cada item de la página.
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h3[contains(@class,"list-item-title")]/a')),
							callback = 'parse_items', follow = True)
	}
    
    def array_to_string(self, array):
        """
        Función que para un array realizará la limpieza necesaria para poder devolver únicamente un string.
        """
        # Se selecciona solo el lo que va entre los símbolos "<" y ">".
        pattern = r"<.*?>"
        formated_array = re.sub(pattern, '', str(array))
        # Se aplican remplazos de caracteres para que coincida con texto en español.
        formated_array = formated_array.replace("\\r\\n", "").replace("\'", "").replace(" ,", ",")
        # Se cambian todos los espacios mayores a dos por un único espacio, se eliminan datos innecesarios y se aplican más remplazos de caracteres para que coincida con el español.
        formated_array = re.sub( "\s{2,}", " ",formated_array).replace("Certificado energético : ", "").replace(" Ver etiqueta calificación energética ", "").replace("m2 / año", "m2/año").replace("año E", "año, E")
        return formated_array
    
    def get_name(self, list, type):
        """
        Función que para una lista de rutas de descarga de imágenes devolverá:
            - Caso (type ='saved_path'): Lista de rutas en las cuales se pueden encontrar dentro del repositorio local.
            - Caso (type ='folder_name'): Nombre de la carpeta en la cual se encuentran las imágenes detro del repositorio local.
            - Caso (type ='names'): Lista de nombres de las imágenes guardadas en el repositorio local.
        """
        # Devolución de los paths en los que se guardarán las imágenes partiendo de la carpeta "dataset".
        if type == "saved_path":          
            new_list = []
            for element in list:
                name = list[0].split("/")[-1]
                index = name.rindex("-")
                folder_name = name[0:index]
                image_name = name[(index + 1):]
                new_list.append("dataset/imagenes/" + folder_name + "/" + image_name)
            return new_list
        # Devolución del nombre de la carpeta en la que se almacenarán las imágenes de los diferentes pisos.
        elif type == "folder_name":
            name = list[0].split("/")[-1]
            index = name.rindex("-")
            folder_name = name[0:index]
            return folder_name
        # Devolución de los nombres que tendrán las diferentes imágenes almacenadas.
        elif type == "names":          
            new_list = []
            for element in list:
                new_list.append(element.split("/")[-1].split("-")[-1])
            return new_list

    def parse_items(self, response):
        """
        Función encargada de parsear todos los elementos que se encuentran en cada una de las páginas en las cuales se hará el web scraping.
        """

        # Se rellenará el item creado con los diferentes campos que se han definido.
        casa = CasaItem()
		# Info referente a cada vivienda.
        casa['name'] = response.xpath('normalize-space(//h1/text())').extract()
        casa['price'] = response.xpath('normalize-space(//div[@class="price"]/span/text())').extract()
        casa['summary'] = self.array_to_string(response.xpath('//article[contains(@id, "js-feature-container")]/ul[contains(@class, "feature-container")]/li').extract()) 
        casa['short_description'] = response.xpath('normalize-space(//h3/text())').extract()
        casa['description'] = response.xpath('normalize-space(//p[@class="detail-description"])').extract()
        casa['last_modified'] = response.xpath('normalize-space(//p[@class="time-tag"]/time/text())').extract()
        casa['distribution'] = response.xpath('//article[@class="has-aside"][2]/ul/li/text()').getall()
        casa['general_characteristics'] = self.array_to_string(response.xpath('//article[@class="has-aside"][3]/ul/li').extract())
		# Info referente a las imágenes de cada vivienda.
        casa['image_urls'] = response.xpath('//section[@id="js-gallery"]/div[2]/div/a/img/@src').extract()
        casa['image_names'] = self.get_name(response.xpath('//section[@id="js-gallery"]/div[2]/div/a/img/@src').extract(), type="names")
        casa['folder1'] = self.get_name(response.xpath('//section[@id="js-gallery"]/div[2]/div/a/img/@src').extract(), type="folder_name")
        casa['saved_path'] = self.get_name(response.xpath('//section[@id="js-gallery"]/div[2]/div/a/img/@src').extract(), type="saved_path")
        yield casa

    
   