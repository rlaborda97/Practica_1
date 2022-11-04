## Máster Universitario de Ciencia de datos. Asignatura: [Tipologia y ciclo de vida de los datos](http://cv.uoc.edu/tren/trenacc/web/GAT_EXP.PLANDOCENTE?any_academico=20222&cod_asignatura=M2.851&idioma=CAS&pagina=PD_PREV_PORTAL&cache=S). Práctica 1. Noviembre 2022.
[texto a mostrar](url completa)
# Web Scraping
***

## Índice
### 1. [Información general](#Información-general)
### 2. [Tecnologías](#tecnologías)
### 3. [Instalación](#Instalación)
### 4. [Licencia](#Licencia)

## 1. [Información general](#Información-general)
El código de este repositorio permite extraer información de pisos de la web [https://www.habitaclia.com/](https://www.habitaclia.com/) y guardarla en un archivo habitaclia_houses.csv
## 2. [Tecnologías](#tecnologías)
* Python 3.10
* Scrapy 2.7.1

Scrapy es una herramienta de extración de datos de Python de código abierto que permite crear arañas web que pueden recorrer diferentes webs para extraer información.  
[https://www.scrapy.org/](https://www.scrapy.org/)  

## 3. [Instalación](#Instalación)  
1. Instalar Scrapy desde el terminal .
`C:...\...> pip install scrapy`  
2. Descargar la carpeta en cualquier directiorio  
3. Abrir un terminal y acceder al directorio donde se encuentre el archivo scrapy.cfg. En este caso es scrapy_project  
`C:...\source\scrapy_project>`
4. Escribir el siguiente código para ejecutar la araña web habitaclia que se encuentra dentro de la carpeta spiders  
`C:...\source\scrapy_project> scrapy crawl habitaclia`  
5. Revisar que la información quedará guardada en el directorio del paso 3. Archivo habitaclia_houses.csv
## 4. [Licencia](#Licencia)
