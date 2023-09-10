import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

siniestros = pd.read_csv('siniestrosEDA.csv')

dia_semana_lista = siniestros['DIA_SEMANA'].unique().tolist()
comuna_lista = siniestros['COMUNA'].unique().tolist()
tipo_calle_lista = siniestros['TIPO_CALLE'].unique().tolist()
acusado_lista = siniestros['ACUSADO'].unique().tolist()
victima_lista = siniestros['VICTIMA'].unique().tolist()
año_lista = siniestros['A'].unique().tolist()
fatal_lista = siniestros['FATAL'].unique().tolist()

dias = st.sidebar.multiselect('Día de la Semana:', dia_semana_lista, default=dia_semana_lista)
comuna = st.sidebar.multiselect('Comuna:', comuna_lista, default=comuna_lista)
tipo_calle = st.sidebar.multiselect('Tipo de Calle:', tipo_calle_lista, default=tipo_calle_lista)
acusado = st.sidebar.multiselect('Acusado:', acusado_lista, default=acusado_lista)
victima = st.sidebar.multiselect('Víctima:', victima_lista, default=victima_lista)
año = st.sidebar.multiselect('Año:', año_lista, default=año_lista)
fatal = st.sidebar.multiselect('Fatalidad:', fatal_lista, default=fatal_lista)

victimas_por_hora3 = siniestros['H'][(siniestros['DIA_SEMANA'].isin(dias)) & (siniestros['COMUNA'].isin(comuna)) &
                                         (siniestros['TIPO_CALLE'].isin(tipo_calle)) & (siniestros['ACUSADO'].isin(acusado)) &
                                         (siniestros['VICTIMA'].isin(victima)) & (siniestros['A'].isin(año))].value_counts().sort_index()

fig3 = plt.figure(figsize=(16, 8))
plt.bar(victimas_por_hora3.index, victimas_por_hora3.values, color='skyblue')
plt.xlabel('Hora del Día')
plt.ylabel('Cantidad de Lesiones')
plt.title('Cantidad de Lesiones por Hora del Día')
plt.xticks(range(24))  # Etiquetas del eje x para cada hora
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig3)