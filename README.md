# My ETL Project:

https://datos.madrid.es/egob/catalogo/209548-491-censo-locales-historico.json = enlace de json
Selenium a Tripadvisor para opiniones
Api place de Google para reseñas

# Proyecto ETL - Google Place API, JSON Descargado y Web Scraping de TripAdvisor

## Introducción
Este proyecto de ETL tiene como objetivo la extracción, transformación y carga de datos relacionados con los restaurantes étnicos de Madrid, con los que queremos estudiar su evolución y factores de éxito. Hemos utilizado varias fuentes de datos, incluyendo la API Place de Google, un archivo JSON descargado y web scraping con Selenium desde la página de TripAdvisor.

## Objetivo

El objetivo principal de este proyecto es consolidar información detallada sobre los restaurantes étnicos en una base de datos centralizada. Para lograr esto, seguimos estos pasos:

1. **Extracción (Extract):** Utilizamos la API Place de Google para obtener datos relacionados con restaurantes étnicos de Madrid, como nombres, direcciones, coordenadas geográficas, reseñas, calificaciones, fotos, etc. Usamos Tripadvisor para consolidar nuestro datos añadiendo mas reseñas. El archivo json se obtuvo de la bas de datos abierto de la Comunidad de Madrid de los cuales no interesa las frchas de apertura y sus localizaciones.

2. **Transformación (Transform):** Los datos extraídos se someten a un proceso de transformación para limpiarlos, estructurarlos y prepararlos para su inserción en una base de datos. Esto incluye la normalización de datos, la conversión de formatos, la agregación de información y la eliminación de datos irrelevantes.

3. **Carga (Load):** Los datos transformados se cargan en una base de datos centralizada, que servirá como fuente de información para aplicaciones y análisis posteriores.

## Fuentes de Datos

### 1. API Place de Google

Hemos utilizado la API Place de Google para obtener información detallada sobre lugares turísticos. Para acceder a esta API, necesitas una clave de API válida de Google. Los datos extraídos incluyen detalles como nombres, direcciones, calificaciones, reseñas y más.

![image]()

### 2. Archivo JSON Descargado

Hemos descargado un archivo JSON desde una fuente externa. Este archivo contiene enlaces a información adicional sobre restaurantes étnicos. Utilizamos este enlace para complementar los datos de la API de Google.

https://datos.madrid.es/egob/catalogo/209548-491-censo-locales-historico.json

### 3. Web Scraping de TripAdvisor

Para enriquecer nuestros datos con reseñas y calificaciones de usuarios, realizamos web scraping en la página de TripAdvisor. Utilizamos la biblioteca Selenium para automatizar la navegación web y extraer información relevante de las páginas de TripAdvisor.
