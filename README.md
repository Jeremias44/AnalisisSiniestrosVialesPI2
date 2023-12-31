<h1 align='center'>
 <b>SINIESTROS VIALES BUENOS AIRES</b>
</h1>

# <h1 align="center">**`Por Jeremías Pombo`**</h1>

<h1 align='center'>
 <b>Análisis de Accidentes de Tránsito en la Ciudad Autónoma de Buenos Aires</b>
</h1>

<p align='center'>
<img src="https://cdn.aarp.net/content/dam/aarp/auto/2021/05/1140-minor-fender-bender-esp.imgcache.rev.web.700.402.jpg" alt="Accidente de tránsito">
</p>

# Introducción

Este proyecto aborda el análisis de datos de accidentes de tránsito en la Ciudad Autónoma de Buenos Aires con el objetivo de proporcionar información crucial para tomar medidas que reduzcan las víctimas fatales en siniestros viales. El proyecto se desarrolla desde un rol de analista de datos, en colaboración con el `Observatorio de Movilidad y Seguridad Vial` (OMSV) de la ***Secretaría de Transporte*** del Gobierno de la Ciudad Autónoma de Buenos Aires y se basa en datos recopilados entre 2016 y 2021.

# Estructura del Proyecto

### Contenido del Repositorio

- **DATOS**:
  - `homicidios.xlsx` y `lesiones.xlsx`: Datasets originales.
  - `siniestrosETL.csv`: Datos extraídos y transformados.
  - `siniestroEDA.csv`: Datos limpiados y listos para análisis.
  - `kpi_1.csv`, `kpi_2.csv`, `kpi_3.csv`: Archivos con indicadores clave.

- **NOTEBOOKS**:
  - `ETL.ipynb`: Proceso de Extracción, Transformación y Carga.
  - `EDA.ipynb`: Análisis Exploratorio de Datos.
  - `Visualizaciones.ipynb`: Visualizaciones y KPI.

- **STREAMLIT**:
  - `Presentación.py`: Aplicación web interactiva.
  - `pages/`: Carpetas con páginas específicas.
  - `requirements.txt`: Lista de bibliotecas necesarias.
  - `mapahomicidios.html`, `mapasiniestros.html`: Mapas consultables a través de Streamlit.

- **GITHUB**:
  - `README.md`: Presentación y explicación del proyecto.
  - `REPORTE.md`: Reporte detallado del proyecto.
  - `.gitignore`: Archivo de excepciones para actualizaciones.
  - `Consigna.md`: Descripción original del proyecto.

- **POWER BI**:
  - `Dashboard/`: Carpeta que contiene el Dashboard en formato .pbix, PDF y PNG
  - `PI2_PowerBi.pbix`: Dashboard interactivo del proyecto.
  - `PI2_PowerBi.pdf`: Dashboard exportado para su visualización rápida.

# Proceso de Trabajo

El análisis se centra en dos bases de datos en archivos Excel: `homicidios.xlsx` y `lesiones.xlsx`, que contienen información sobre accidentes de tránsito en la Ciudad de Buenos Aires. Estos datos se someten a un proceso de ETL para unificar y limpiar los datos. Luego, se realiza un análisis exploratorio de datos (EDA) para comprender las tendencias y patrones clave.

### Paso 1: ETL

- Extracción, transformación y carga de datos de `homicidios.xlsx` y `lesiones.xlsx`.
- Unión de datos de víctimas fatales y víctimas con lesiones en un solo DataFrame.

### Paso 2: EDA

- Normalización de tipos de datos y limpieza.
- Visualización y análisis inicial.
- Creación de `siniestrosEDA.csv` para su uso en Streamlit y Power BI.

### Paso 3: Visualizaciones y KPI

- Creación de visualizaciones específicas y cálculo de KPI en `Visualizaciones.ipynb`.
- Generación de archivos `kpi_1.csv`, `kpi_2.csv`, y `kpi_3.csv` para su consulta en Streamlit y Power BI.

### Paso 4: Streamlit

- Desarrollo de una aplicación web interactiva con Streamlit.
- Presentación de datos a través de gráficos, botones y filtros.

### Paso 5: Power BI

- Creación de un dashboard interactivo y un informe de análisis.

***

`A continuación se presenta un resumen del reporte. Para visualizar el reporte completo se sugiere la lectura del archivo REPORTE.md`

# Hallazgos y Patrones en los Datos

Durante el análisis de los datos, se destacaron hallazgos importantes:

- El 98.9% de los accidentes viales resulta en lesiones leves o graves, mientras que el 1.1% son fatales.
- Los motociclistas tienen una alta probabilidad de sufrir accidentes fatales (2.7% de los accidentes de motociclistas).
- Los peatones también están en riesgo (6% de los accidentes resultan en víctimas fatales).
- Los autos particulares son los principales responsables de accidentes, pero los transportes de carga, pasajeros y objetos fijos tienen mayor tasa de fatalidad.
- Los sábados y domingos son días de menos accidentes pero más fatalidades, especialmente en autopistas y avenidas principales.

# Conclusiones

Basado en el análisis, se pueden concluir los siguientes puntos:

- Los accidentes en horarios de madrugada los fines de semana están relacionados con conductores alcoholizados y alta velocidad.
- Los accidentes en diciembre tienen una alta tasa de fatalidad, especialmente en autopistas.
- Durante diciembre y enero, aumenta la presencia de conductores ocasionales, lo que coincide con vehículos en mal estado y conductores menos experimentados.
- La mayoría de los accidentes en horario laboral resultan en lesiones menores.

# Recomendaciones

Se sugieren las siguientes medidas para reducir la tasa de accidentes fatales:

- Aumentar los controles de verificación técnica vehicular en noviembre, diciembre y enero.
- Reforzar los controles de alcoholemia los viernes de 21hs a sábados 7hs y sábados de 22hs a domingos 8hs.
- Prohibir la circulación y carga de vehículos de carga en áreas restringidas de lunes a viernes de 7 a 10hs y de 15 a 18hs, especialmente en comunas 1, 4 y 9.
- Implementar campañas de concientización sobre el uso del casco para motociclistas y ciclistas, con multas por infracciones.
- Aumentar los controles de velocidad y uso del cinturón de seguridad en autopistas y peajes los domingos.
- Concientizar sobre las maniobras peligrosas en avenidas y sus consecuencias fatales, como el estacionamiento en doble fila y los cambios de carril sin aviso previo.

***

# Enlaces y Links de Consulta

### Enlaces Principales:

* [Video de Presentación del Informe](https://youtu.be/FA8Fndmutn4?si=6xv35AGshB3oQt35)
* [Repositorio de GitHub](https://github.com/Jeremias44/Proyecto_Individual_2.git)
* [Imágenes y PDF Dashboard](https://github.com/Jeremias44/Proyecto_Individual_2/tree/main/Dashboard)
* [Reporte Completo](https://github.com/Jeremias44/Proyecto_Individual_2/blob/main/REPORTE.md)
* [Linkedin](https://www.linkedin.com/in/jeremiaspombo/)

### Otros Enlaces

* [Enlace a Dashboard Interactivo](https://www.novypro.com/project/informe-de-siniestros-viales-en-la-ciudad-de-buenos-aires---2016-a-2021)
* [Enlace a Streamlit](https://proyectoindividual2jeremiaspombo.streamlit.app/)

***

#### El presente trabajo fue realizado por Jeremías Pombo utilizando:
* Bibliotecas seaborn, pandas, numpy, matplotlib, folium de Python
* Streamlit de manera local y de manera remota a través de una url en la web.
* Novypro y Microsoft Azure 
* Power Bi y Power Service
