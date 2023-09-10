import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

siniestros = pd.read_csv('siniestrosEDA.csv')
homicidios = siniestros[siniestros['FATAL']==1]

st.sidebar.write('Accidentes por Hora')
min_value1, max_value1 = st.sidebar.slider('Rango Años - Homicidios', 2016, 2021, (2019,2021))
min_value2, max_value2 = st.sidebar.slider('Rango Años - Lesiones', 2019, 2021, (2019,2021))


victimas_por_hora1 = homicidios['H'][(homicidios['A'] <= max_value1) & (homicidios['A'] >= min_value1)].value_counts().sort_index()
fig1 = plt.figure(figsize=(12, 3))
plt.bar(victimas_por_hora1.index, victimas_por_hora1.values, color='skyblue')
plt.xlabel('Hora del Día')
plt.ylabel('Cantidad de Víctimas Fatales')
plt.title('Cantidad de Víctimas Fatales por Hora del Día')
plt.xticks(range(24))  # Etiquetas del eje x para cada hora
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig1)

victimas_por_hora2 = siniestros['H'][(siniestros['A'] <= max_value2) & (siniestros['A'] >= min_value2)].value_counts().sort_index()
fig2 = plt.figure(figsize=(12, 3))
plt.bar(victimas_por_hora2.index, victimas_por_hora2.values, color='skyblue')
plt.xlabel('Hora del Día')
plt.ylabel('Cantidad de Lesiones')
plt.title('Cantidad de Lesiones por Hora del Día')
plt.xticks(range(24))  # Etiquetas del eje x para cada hora
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig2)