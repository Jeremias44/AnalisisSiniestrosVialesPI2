import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



kpi_1 = pd.read_csv('kpi_1.csv')
kpi_2 = pd.read_csv('kpi_2.csv')
kpi_3 = pd.read_csv('kpi_3.csv')

    
if st.checkbox('Descripciones de KPI'):
    st.write('KPI 1: Reducir 10% la tasa de homicidios en siniestros viales respecto al semestre anterior')    
    st.write('KPI 2: Reducir 7% la tasa de homicidios en siniestros viales con motos respecto al año anterior')
    st.write('KPI 3: Reducir 10% la tasa de homicidios en siniestros viales con peatones respecto al año anterior')

if st.checkbox('tablas'):      
    tablas = st.radio('Visualizar tablas de KPI:',('KPI 1','KPI 2', 'KPI 3', 'cerrar'), horizontal=True)
    if tablas == 'KPI 1':
        st.dataframe(kpi_1[['A','SEMESTRE','TASA_HOMICIDIOS','TASA_SEMESTRE_ANTERIOR','VARIACION']])
    if tablas == 'KPI 2':
        st.dataframe(kpi_2[['A','TASA_HOMICIDIOS','TASA_AÑO_ANTERIOR','VARIACION']])
    if tablas == 'KPI 3':
        st.dataframe(kpi_3[['A','TASA_HOMICIDIOS','TASA_AÑO_ANTERIOR','VARIACION']])
    if tablas == 'cerrar':
        pass

if st.checkbox('gráficos'):
    grafico = st.radio('Visualizar gráficas de KPI:',('KPI 1','KPI 2', 'KPI 3','cerrar'), horizontal=True)

    if grafico == 'KPI 1':
        kpi_1['SEMESTRE'] = [6 if a == 2 else a for a in kpi_1['SEMESTRE']]
        kpi_1['A'] = pd.to_numeric(kpi_1['A'], errors='coerce')
        kpi_1['SEMESTRE'] = pd.to_numeric(kpi_1['SEMESTRE'], errors='coerce')
        kpi_1 = kpi_1.dropna(subset=['A', 'SEMESTRE'])
        kpi_1['A'] = kpi_1['A'].astype(int)
        kpi_1['SEMESTRE'] = kpi_1['SEMESTRE'].astype(int)
        kpi_1['FECHA'] = kpi_1['A'].astype(str) + '-' + kpi_1['SEMESTRE'].astype(str) + '-01'
        kpi_1['FECHA'] = pd.to_datetime(kpi_1['FECHA'], format='%Y-%m-%d')

        plt.figure(figsize=(12, 6))
        colores = ['skyblue' if valor < -10 else 'gray' for valor in kpi_1['VARIACION']]
        plt.bar(kpi_1['FECHA'], kpi_1['VARIACION'], color=colores, width=90)
        plt.xlabel('Año y Semestre')
        plt.ylabel('Variación')
        plt.title('Variación por Semestre a lo largo del Tiempo')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        st.pyplot(plt)

    if grafico == 'KPI 2':
        plt.figure(figsize=(12, 6))
        colores = ['skyblue' if valor < -7 else 'gray' for valor in kpi_2['VARIACION']]
        plt.bar(kpi_2['A'], kpi_2['VARIACION'], color=colores, width=0.5)
        plt.xlabel('Año')
        plt.ylabel('Variación')
        plt.title('Variación por año')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        st.pyplot(plt)

    if grafico == 'KPI 3':
        plt.figure(figsize=(12, 6))
        colores = ['skyblue' if valor < -10 else 'gray' for valor in kpi_3['VARIACION']]
        plt.bar(kpi_3['A'], kpi_3['VARIACION'], color=colores, width=0.5)
        plt.xlabel('Año')
        plt.ylabel('Variación')
        plt.title('Variación por año')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        st.pyplot(plt)

    if grafico == 'cerrar':
        pass