<h1 align='center'>
 <b>PROYECTO INDIVIDUAL Nº2</b>
</h1>

# <h1 align="center">**`Por Jeremías Pombo`**</h1>

<h1 align='center'>
 <b>Análisis de accidentes de tránsito en la Ciudad Autónoma de Buenos Aires</b>
</h1>





# Introducción

### El presente proyecto consta de simular el siguiente escenario:

El `Observatorio de Movilidad y Seguridad Vial` (OMSV), bajo la órbita de la ***Secretaría de Transporte*** del Gobierno de la Ciudad Autónoma de Buenos Aires, solicita la elaboración de un proyecto de anális de datos, con el fin de generar información que permita tomar medidas para disminuir la cantidad de víctimas fatales en siniestros viales. Se cuenta con un dataset sobre homicidios en siniestros viales acaecidos en la Ciudad de Buenos Aires durante el período 2016-2021.

***
***

# Estructura del proyecto

### En el presente repositorio vas a encontrar:

DATOS:
* Los archivos homicidios.xlsx y lesiones.xlsx, son los dataset originales a partir del cual se realiza el ETL y el EDA correspondiente
* El archivo siniestrosETL.csv, con los datos ya extraídos, transformados en sus aspectos principales y unidos bajo un solo DataFrame.
* El archivo siniestroEDA.csv, con los datos ya analizados en una primera revisión, con limpieza realizada (imputaciones, manejo de errores, nulos y duplicados) y listo para ser trabajado tanto en Power Bi como en Streamlit.
* Los archivos kpi_1.csv, kpi_2.csv y kpi_3.csv, cada uno con su respectivo DataFrame con las medidas correspondientes a cada KPI.

NOTEBOOKS:
* ETL.ipynb (proceso de extracción, transformación y carga de archivos).
* EDA.ipynb (proceso de análisis exploratorio de datos).
* Visualizaciones.ipynb (proceso de EDA y su continuación con visualizaciones específicas, incluídos los KPI).

STREAMLIT:
* Presentación.py es el archivo madre donde se crea la app que será consultada en la web de Streamlit
* pages, carpeta que contiene los distintos archivos .py con las páginas que se visualizarán en la web de Streamlit (carpeta)
* requirements.txt, bibliotecas necesarias para correr los archivos .py en Streamlit
* mapahomicidios.html, mapasiniestros.html, mapas que serán consultados a través de Streamlit

GITHUB
* .gitignore, archivo de excepciones de actualización al repositorio de GitHub
* README.md, presentación y explicación del Proyecto Individual 2
* Consigna.md, consigna original del Proyecto Individual 2

POWER BI
* PI2_PowerBi.pbix, archivo Power Bi con el dashboard del proyecto, más páginas de presentación e informes.

***
***

# Proceso de Trabajo

### Para el análisis se cuenta con dos bases de datos en archivos Excel:

* homicidios.xlsx, donde se registran dos tablas:
    - HECHOS: 696 casos de accidentes con víctimas fatales
    - VICTIMAS: 717 víctimas fatales, producto de los 696 hechos mencionados

* lesiones.xlsx, donde se registran dos tablas:
    - HECHOS: 23785 casos de accidentes con víctimas lesionadas
    - VICTIMAS: 27605 víctimas lesionadas, producto de los 23785 hechos mencionados

* información relevante:

    24481 siniestros totales, 696 siniestros con víctima fatal, 23785 siniestros con víctima lesionada

    28322 víctimas totales, 717 víctimas fatales, 27605 víctimas con lesiones

### El primer paso es hacer un ETL (extracción, transformación y carga) de datos, que combine las tablas de cada archivo excel, normalizando nombres de columnas, y filtrando únicamente las columnas que utilizaremos para el análisis posterior. Luego de ello se unen las dos tablas (HECHOS Y VICTIMAS) en cada uno de los casos (homicidios y lesiones), y se concatenan los dos dataframes resultantes (homicidios y lesiones) bajo el nombre de siniestros.

* En el archivo ETL.ipynb se realiza:

    - 1) La extracción, transformación y carga de los datos de homicidios.xlsx, devolviendo un df 'homicidios' que contiene 717 registros de víctimas fatales asociadas con los 696 hechos a través de un ID. (exportado como 'homicidiosETL.csv')

    - 2) La extracción, transformación y carga de los datos de lesiones.xlsx, devolviendo un df 'lesiones' que contiene 27605 registros de víctimas con lesiones asociadas con los 23785 hechos a través de un ID. (exportado como 'lesionesETL.csv')

    - 3) La concatenación de ambos df (homicidios y lesiones), en un archivo total, llamado siniestrosETL.csv, donde se encuentran los 28322 registros totales que incluyen las 28322 víctimas (717 fatales + 27605 lesionadas) y se relacionan con un hecho específico de los 24481 hechos registrados (23785 con lesiones + 696 con víctimas fatales).

###### NOTA: Se decide hacer la unión de las tablas 'HECHOS' y 'VICTIMAS' debido a la poca variación que implica en cuanto al número de filas, y para obtener un solo df con toda la información de ambas tablas, sin que esto implique un crecimiento excesivo de filas. (Menos del 1% de los hechos tienen más de una víctima)

### El segundo paso es hacer un EDA (análisis exploratorio de datos) donde se normaliza el tipo de datos de cada columna, se realizan las imputaciones correspondientes procurando no eliminar ningún dato, y se realizan las primeras visualizaciones para comprender los datos, aplicando filtros correspondientes

* En el archivo EDA.ipynb se realiza:

    - Normalización del tipo de datos de cada columna (para esto se realizan las imputaciones previas necesarias)

    - Visualización de los datos totales

    - Creación del archivo 'siniestrosEDA.csv' listo y disponible para trabajarlo con Streamlit y Power Bi.

### El tercer paso es hacer las visualizaciones y análisis correspondientes en un archivo .ipynb, para obtener visualizaciones claras y específicas, que aporten valor al entendimiento del problema.

* En el archivo visualizaciones.ipynb se importa la tabla 'siniestrosEDA.csv' y se trabajan las consultas necesarias, comenzando con los tres KPIS principales y continuando con otras visualizaciones más específicas.

* Se crean los archivos kpi_1.csv, kpi_2.csv, kpi_3.csv. Serán consultados luego en Presentación.py con Streamlit, y también en el dashboard con Power Bi

### El cuarto paso es, utilizando la biblioteca Streamlit, obtener visualizaciones claras y específicas, que aporten valor al entendimiento del problema, que sean amigables con el usuario a través de botones, barras deslizantes y filtros interactivos. Este archivo será disponibilizado a través de una web

* En el archivo Presentación.py se importan los csv necesarios para trabajarlos y disponibilizar su visualización en la web.

### El quinto paso es la creación de un dashboard interactivo y un informe del análisis en Power Bi

* En el archivo PI2_PowerBi.pbix se encuentra el informe referido. Se puede consultar desde la web.

***
***

# Reporte de Análisis y Hallazgos

### Principales hallazgos observados a lo largo del estudio de los datos. Análisis del impacto de ciertas variables en el desenlace de víctimas fatales en accidentes de tránsito. Análisis de la funcionalidad y resultados de los KPIs propuestos.

SE OBSERVAN LOS SIGUIENTES PATRONES Y RELACIONES ENTRE VARIABLES:

* Baja en la tasa de siniestros viales, acompañada de una baja en la tasa de víctimas fatales en los últimos años
* El último año analizado (2021) se encuentra con altos valores respecto al año anterior, pero no debe preocupar ya que se debe a la pronunciada baja que hubo durante el año 2020 debido a la restricciones de circulación por la pandemia. Si se observa con una visión más amplia, se nota que la tendencia sigue siendo a la baja.
* Los horarios donde mayor cantidad de accidentes con lesiones se producen son entre las 12 y las 19hs, especialmente de lunes a viernes.
* Los horarios donde mayor cantidad se accidentes fatales se producen son entre las 5 y las 7hs, especialmente los días sábados y domingos.
* La mayoría de los accidentes ocurren en avenidas. La avenida General Paz es un gran foco de accidentes viales.
* Los días sábados y domingos son los días de menor cantidad de accidentes, pero los de mayor cantidad de víctimas fatales.
* Los accidentes con mayor ocurrencia de fatalidad en proporción son los ocasionados en autopistas.
* Los autos son los que más muertes provocan.
* Los motociclistas y los petaones son los que mayor posibilidad de desenlace fatal poseen.

***
***

# Conclusiones

### Conclusiones en base a los hallazgos realizados.

EN BASE AL ANÁLISIS DEL INFORME SE PUEDE CONCLUIR:

* Los accidentes ocurridos Sábados y Domingos entre las 4 y las 7 a.m. tienen una alta tasa de fatalidad; se evidencia que son accidentes provocados por conductores alcoholizados, y altas velocidades.
* Los accidentes ocurridos en el mes de diciembre tienen una alta tasa de fatalidad; se evidencia mayor ocurrencia en autopistas.
* Durante los meses de Diciembre y Enero circulan conductores "de ocasión". Hay mayor cantidad de autos en mal estado, y conductores poco experimentados, coincidente con períodos no laborales. Quienes utilizan el auto a diario, por lo contrario tienen autos más seguros y en mejores condiciones.
* La gran mayoría de los accidentes ocurren de lunes a viernes entre las 12 y las 18hs. En esta franja horaria el porcentaje de víctimas fatales es menor al 0,5% por lo que se entiende que estos son accidentes "menores".

***
***

# Decisiones a tomar

### Recomendaciones basadas en los resultados obtenidos del estudio, con el fin de bajar la tasa de accidentes fatales en la Ciudad de Buenos Aires.

Luego del reporte de análisis y las conclusiones, se recomiendan las siguientes medidas:


* Duplicar los controles de verificación técnica vehicular durante los meses de Noviembre, Diciembre y Enero.
* Duplicar controles de alcoholemia con retención de vehículos en los siguientes horarios:

Viernes 21hs a Sábados 7hs

Sábados 22hs a Domingos 8hs
* Prohibición de circulación, carga y descarga de vehículos de carga en sectores restringidos de la ciudad de lunes a viernes de 7 a 10 y de 15 a 18hs. Especialmente en comunas 1, 4 y 9.
* Campañas de concientización para el uso de casco en motociclistas y ciclistas. Implementación de altas multas para quienes incurran en contravención.
* Duplicar controles de velocidad y uso del cinturón de seguridad en autopistas y peajes, los días domingo.
* Concientizar sobe el peligro de maniobras peligrosas en avenidas y sus consecuencias fatales, como estacionamientos en doble fila y cambios de carril.
* Descomprimir el tránsito de la avenida General Paz, implementar junto a autoridades de la provincia de Buenos Aires un plan de obras de circunvalación por fuera del casco de la Ciudad de Buenos Aires,  (la Av. Gral. Paz es un gran foco de accidentes viales y atascamientos del tránsito).
* Educar a peatones sobre el ascenso y descenso de la acera. Gran cantidad de muertes de peatones se da al subir/bajar de un vehículo.

***
***

# Enlaces y links de consulta

### A continuación se proporcionan los enlaces para las páginas web de consulta de Streamlit, de Power Service, el link del repositorio de GitHub y el link del video de presentación del informe del proyecto.

* link1
* link2
* link3
* link4

***
***

###### El presente trabajo fue íntegramente realizado por Jeremías Pombo utilizando:
###### * Bibliotecas seaborn, pandas, numpy, matplotlib, folium de Python
###### * Streamlit de manera local y de manera remota a través de la web
###### * Power Bi y Power Service

***
***



