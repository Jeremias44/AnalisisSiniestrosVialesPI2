import streamlit as st

# Define colores hexadecimales
amarillo = "#FDD306"
celeste = "#0089F1"
gris_oscuro = "#706F6F"
gris = "#A7A6A6"
gris_claro = "#C6C6C4"

# Configura el título con color celeste
st.markdown('<h1 style="color: {};">Análisis de Accidentes de Tránsito en la Ciudad Autónoma de Buenos Aires</h1>'.format(celeste), unsafe_allow_html=True)
st.markdown('<h1 style="color: {};">Presentación del Problema</h1>'.format(gris), unsafe_allow_html=True)

# Línea divisoria en color gris claro
st.markdown(f'<hr style="border:2px solid {gris_claro}">', unsafe_allow_html=True)

# Párrafo de introducción en color gris oscuro
st.markdown('''
Este proyecto aborda el análisis de datos de accidentes de tránsito en la Ciudad Autónoma de Buenos Aires con el objetivo de proporcionar información crucial para tomar medidas que reduzcan las víctimas fatales en siniestros viales. El proyecto se desarrolla en colaboración con el <i>Observatorio de Movilidad y Seguridad Vial</i> (OMSV) de la <b>Secretaría de Transporte</b> del Gobierno de la Ciudad Autónoma de Buenos Aires y se basa en datos recopilados entre 2016 y 2021.
''', unsafe_allow_html=True)

# Barra lateral con enlace en color amarillo
st.sidebar.markdown(f'<a href="#">Más</a>', unsafe_allow_html=True)

