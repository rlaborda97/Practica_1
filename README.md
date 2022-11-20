# Práctica 1 - Tipología y Ciclo de Vida de los Datos
Asignatura: M2.851 / Fecha: 22-11-2022

## Autores
  * Raúl Laborda Nicolás - [rlabordan@uoc.edu](rlabordan@uoc.edu)
  * Fèlix Moisès Cordero Rangel - [fcorderora@uoc.edu](fcorderora@uoc.edu)

## Descripción del repositorio.
El siguiente proyecto se basa en una spyder desarrollada con la librería Scrapy que almacena todos los datos de los diferentes anuncios de viviendas de la página habitaclia en La Ñora.

### Estructura.

  * `Practica1_Felix_Raul.pdf`: Documentación asociada al proyecto presentada por los dos alumnos.
  * `ENLACES_VIDEO.txt`: Documentación asociada al almacenamiento del vídeo del proyecto.
  * `LICENSE.txt`: Documentación asociada a la licencia del proyecto.
  * `/source/requirements.txt`: Fichero que contiene las librerías utilizadas en el environment con el cual se puede ejecutar y trabajar con el proyecto.
  * `/source/scrapy_project/first_project/spiders/habitaclia.py`: Archivo principal con la araña.
  * `/source/scrapy_project/first_project/items.py`: Archivo con el formato del objeto a rellenar por la araña con cada anuncio.
  * `/source/scrapy_project/first_project/get_techs.py`: Archivo con código para obtener las tecnologías de la página web.
  * `/source/scrapy_project/first_project/pipelines.py`: Archivo con las pipelines que utilizará la araña para almacenar tanto los datos como las imágenes.
  * `/source/scrapy_project/first_project/settings.py`: Archivo con la configuración de todo el proyecto.
  * `/source/scrapy_project/first_project/items.py`: Archivo con el formato del objeto a rellenar por la araña con cada anuncio.
  * `/dataset/habitaclia_houses.csv`: Fichero csv con todos los datos de cada uno de los anuncios.
  * `/dataset/imagenes`: La carpeta imágenes contiene un conjunto de subcarpetas, una para cada anuncio con las diferentes imágenes de dicho anuncio.

## Publicación en Zenodo
El dataset ha sido publicado en Zenodo con DOI [10.5281/zenodo.7316460](https://doi.org/10.5281/zenodo.7316460).

## Vídeo de presentación
Enlace al vídeo de presentación de la práctica: [https://drive.google.com/drive/folders/1qR86c_AFlnMlBZ7qzoTJj33feom3R3TM?usp=share_link](https://drive.google.com/drive/folders/1qR86c_AFlnMlBZ7qzoTJj33feom3R3TM?usp=share_link)