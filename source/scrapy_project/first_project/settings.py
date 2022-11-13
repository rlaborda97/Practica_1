# Definición de los parámetros generales del proyecto.
BOT_NAME = 'habitaclia'
SPIDER_MODULES = ['first_project.spiders']
NEWSPIDER_MODULE = 'first_project.spiders'

# Definición de los Pipelines que se van a utilizar y su nivel de importancia.
ITEM_PIPELINES = {'first_project.pipelines.HousesPipeline': 500,
                  'first_project.pipelines.HousesImagesPipeline': 1}

# Definición de la ruta en la cual se almacenarán las imágenes del Pipeline "HousesImagesPipeline".
IMAGES_STORE = '../../../dataset/imagenes'

# Definición del delay entre descargas para que la página web no detecte que somos un bot y no saturar el servidor.
DOWNLOAD_DELAY = 2

# Definición del USER_AGENT a utilizar para que no se nos detecte como scrapers.
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

# Obligación de respetar las políticas impuestas en el fichero "robots.txt"
ROBOTSTXT_OBEY = True

# Desabilitar cookies.
COOKIES_ENABLED = False

# Configuración por defecto.
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
