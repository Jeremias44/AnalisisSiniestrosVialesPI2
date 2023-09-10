# Caso de Estudio: Análisis de accidentes de tránsito en la Ciudad Autónoma de Buenos Aires

### En base al análisis de casos de accidentes de tránsito con víctimas fatales en CABA, se decide evaluar las variables que determinan la disminución o aumento de estos casos, las tasas de víctimas fatales respecto a la población y las tasas de víctimas fatales respecto a los accidentes con víctimas lesionadas.

***
***

# Introducción

### 

***
***

# Estructura del proyecto

### Para el análisis se cuenta con dos bases de datos en archivos Excel:

* homicidios.xlsx, donde se registran dos tablas:
    - HECHOS: 696 casos de accidentes con víctimas fatales
    - VICTIMAS: 717 víctimas fatales, producto de los 696 hechos mencionados

* lesiones.xlsx, donde se registran dos tablas:
    - HECHOS: 23785 casos de accidentes con víctimas lesionadas
    - VICTIMAS: 27605 víctimas lesionadas, producto de los 23785 hechos mencionados

* información relevante:

    siniestros totales: 24481
    siniestros con víctima fatal: 696
    siniestrso con víctima lesionada: 23785

    víctimas totales: 28322
    víctimas fatales: 717
    víctimas con lesiones: 27605

### El primer paso es hacer un ETL (extracción, transformación y carga) de datos, que combine las tablas de cada archivo excel, normalizando nombres de columnas, y filtrando únicamente las columnas que utilizaremos para el análisis posterior. Luego de ello se hace un join entre las dos tablas (HECHOS Y VICTIMAS) en cada uno de los casos (homicidios y lesiones), y una concatenación entre los dos dataframes resultantes (homicidios y lesiones) bajo el nombre de siniestros.

* En el archivo ETL.ipynb se realiza:

    - 1) La extracción, transformación y carga de los datos de homicidios.xlsx, devolviendo un df 'homicidios' que contiene 717 registros de víctimas fatales asociadas con los 696 hechos a través de un ID. (exportado como 'homicidiosETL.csv')

    - 2) La extracción, transformación y carga de los datos de lesiones.xlsx, devolviendo un df 'lesiones' que contiene 27605 registros de víctimas con lesiones asociadas con los 23785 hechos a través de un ID. (exportado como 'lesionesETL.csv')

    - 3) La concatenación de ambos df (homicidios y lesiones), en un archivo total, llamado siniestrosETL.csv, donde se encuentran los 28322 registros totales que incluyen las 28322 víctimas (717 fatales + 27605 lesionadas) y se relacionan con un hecho específico de los 24481 hechos registrados (23785 con lesiones + 696 con víctimas fatales).

###### NOTA: Se decide hacer la unión (merge) de las tablas 'HECHOS' y 'VICTIMAS' debido a la poca variación que implica en cuanto al número de filas, y para obtener un solo df con toda la información de ambas tablas, sin que esto implique un crecimiento excesivo de filas. (Menos del 1% de los hechos tienen más de una víctima)

### El segundo paso es hacer un EDA (análisis exploratorio de datos) donde se normaliza el tipo de datos de cada columna, se realizan las imputaciones correspondientes procurando no eliminar ningún dato, y se realizan las primeras visualizaciones para comprender los datos, aplicando filtros correspondientes

* En el archivo EDA.ipynb se realiza a partir del archivo 'siniestrosETL.csv':

    - Normalización del tipo de datos de cada columna. Para esto se realizan las imputaciones previas necesarias.

    - Visualización de los datos totales

    - Creación del archivo 'siniestrosEDA.csv' listo y disponible para trabajarlo con Streamlit para hacer las visualizaciones interactivas que serán analizadas en detalle y presentadas en el dashboard correspondiente.

### El tercer paso es hacer las visualizaciones y análisis correspondientes en un archivo .ipynb, para obtener visualizaciones claras y específicas, que aporten valor al entendimiento del problema.

* En el archivo visualizaciones.ipynb se importa la tabla 'siniestrosEDA.csv' y se trabajan todas las consultas necesarias, comenzando con los tres KPIS principales y continuando con otras visualizaciones más específicas.

* Se crean los archivos kpi_1.csv, kpi_2.csv, kpi_3.csv. Serán consultados en app.py con streamlit

### El cuarto y último paso es utilizando la biblioteca Streamlit, obtener visualizaciones claras y específicas, que aporten valor al entendimiento del problema, que sean amigables con el usuario a través de botones, barras deslizantes y filtros interactivos. Este archivo será disponibilizado a través de una web

* En el archivo app.py se importaran los csv necesarios para trabajarlos y disponibilizar su visualización en la web

***
***

# Análisis y hallazgos

### Delinearemos los principales hallazgos observados a lo largo del estudio de los datos, y un análisis que busca mostrar el impacto de ciertas variables en el desenlace de víctimas fatales en accidentes de tránsito

* En el estudio de accidentes fatales y no fatales nos centraremos en los años 2019 a 2021 únicamente
* 

***
***

# Conclusiones

### Delinearemos algunas posibles decisiones a tomar, así como recomendaciones basadas en los resultados obtenidos del estudio, para continuar bajando año tras año la tasa de accidentes de tránsito en CABA, y en específico la tasa de accidentes fatales

***
***