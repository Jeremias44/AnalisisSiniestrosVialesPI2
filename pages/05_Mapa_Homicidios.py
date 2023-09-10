import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium

siniestros = pd.read_csv('siniestrosEDA.csv')
homicidios = siniestros[siniestros['FATAL']==1]

# Lista de latitudes y longitudes de ejemplo
latitudes = siniestros.LATITUD.tolist()
longitudes = siniestros.LONGITUD.tolist()

# Crear un mapa centrado en la ubicación promedio de latitud y longitud
mapa = folium.Map(location=[sum(latitudes)/len(latitudes), sum(longitudes)/len(longitudes)], zoom_start=12)

# Agregar un marcador en el mapa para cada par de latitud y longitud
for lat, lon in zip(latitudes, longitudes):
    folium.Marker([lat, lon]).add_to(mapa)

mapa.save("mapahomicidios.html")

# Leer el contenido del archivo HTML generado por Folium
with open("mapahomicidios.html", "r") as f:
    mapa_html = f.read()

# Mostrar el contenido HTML en Streamlit
st.components.v1.html(mapa_html, width=800, height=600)