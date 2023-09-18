import streamlit as st

# Define colores hexadecimales
amarillo = "#FDD306"
celeste = "#0089F1"
gris_oscuro = "#706F6F"
gris = "#A7A6A6"
gris_claro = "#C6C6C4"

# Título de la página de resumen
st.markdown('<h1 style="color: {};">Resumen del Proyecto</h1>'.format(celeste), unsafe_allow_html=True)

# Texto principal
st.markdown('''
Esta visualización interactiva en Streamlit es una demostración de la capacidad interactiva de la herramienta. Para acceder al proyecto completo y obtener información detallada, te invitamos a consultar el archivo **REPORTE.md** y las visualizaciones del dashboard en formato PDF o el archivo **PI2_PowerBi.pbix**.
''', unsafe_allow_html=True)

# Título de Hallazgos y Patrones en los Datos
st.markdown('<h2 style="color: {};">Hallazgos y Patrones en los Datos</h2>'.format(gris), unsafe_allow_html=True)

# Lista de hallazgos
st.markdown('''
- El 98.9% de los accidentes viales resulta en lesiones leves o graves, mientras que el 1.1% son fatales.
- Los motociclistas tienen una alta probabilidad de sufrir accidentes fatales (2.7% de los accidentes de motociclistas).
- Los peatones también están en riesgo (6% de los accidentes resultan en víctimas fatales).
- Los autos particulares son los principales responsables de accidentes, pero los transportes de carga, pasajeros y objetos fijos tienen mayor tasa de fatalidad.
- Los sábados y domingos son días de menos accidentes pero más fatalidades, especialmente en autopistas y avenidas principales.
''')

# Título de Conclusiones
st.markdown('<h2 style="color: {};">Conclusiones</h2>'.format(gris), unsafe_allow_html=True)

# Lista de conclusiones
st.markdown('''
- Los accidentes en horarios de madrugada los fines de semana están relacionados con conductores alcoholizados y alta velocidad.
- Los accidentes en diciembre tienen una alta tasa de fatalidad, especialmente en autopistas.
- Durante diciembre y enero, aumenta la presencia de conductores ocasionales, lo que coincide con vehículos en mal estado y conductores menos experimentados.
- La mayoría de los accidentes en horario laboral resultan en lesiones menores.
''')

# Título de Recomendaciones
st.markdown('<h2 style="color: {};">Recomendaciones</h2>'.format(gris), unsafe_allow_html=True)

# Lista de recomendaciones
st.markdown('''
- Aumentar los controles de verificación técnica vehicular en noviembre, diciembre y enero.
- Reforzar los controles de alcoholemia los viernes de 21hs a sábados 7hs y sábados de 22hs a domingos 8hs.
- Prohibir la circulación y carga de vehículos de carga en áreas restringidas de lunes a viernes de 7 a 10hs y de 15 a 18hs, especialmente en comunas 1, 4 y 9.
- Implementar campañas de concientización sobre el uso del casco para motociclistas y ciclistas, con multas por infracciones.
- Aumentar los controles de velocidad y uso del cinturón de seguridad en autopistas y peajes los domingos.
- Concientizar sobre las maniobras peligrosas en avenidas y sus consecuencias fatales, como el estacionamiento en doble fila y los cambios de carril sin aviso previo.
''')

# Separador
st.markdown(f'<hr style="border:2px solid {gris_claro}">', unsafe_allow_html=True)

# Enlaces y Links de Consulta
st.markdown('<h2>Enlaces y Links de Consulta</h2>', unsafe_allow_html=True)

# Enlaces Principales
st.markdown('''
- [Video de Presentación del Informe](https://youtu.be/FA8Fndmutn4?si=6xv35AGshB3oQt35)
- [Repositorio de GitHub](https://github.com/Jeremias44/Proyecto_Individual_2.git)
- [Imágenes Dashboard](https://github.com/Jeremias44/Proyecto_Individual_2/tree/main/Dashboard)
- [Reporte Completo](https://github.com/Jeremias44/Proyecto_Individual_2/blob/main/REPORTE.md)
- [Linkedin](https://www.linkedin.com/in/jeremiaspombo/)
''', unsafe_allow_html=True)

# Otros Enlaces
st.markdown('''
- [Enlace a Power Service](https://app.powerbi.com/links/7dx9UBe8fp?ctid=811b5463-d762-4cb5-9e0c-4f3f84c975cb&pbi_source=linkShare)
- [Enlace a Streamlit](https://proyectoindividual2jeremiaspombo.streamlit.app/)
''')

# Créditos
st.markdown('''
#### El presente trabajo fue realizado por Jeremías Pombo utilizando:
- Bibliotecas seaborn, pandas, numpy, matplotlib, folium de Python
- Streamlit de manera local y de manera remota a través de una URL en la web
- Power Bi y Power Service
''')

