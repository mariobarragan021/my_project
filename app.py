import pandas as pd
import streamlit as st
import matplotlib as plt
import plotly.express as px


data=pd.read_csv('./vehicles_us.csv')

data.info()

#st.header('Datos de Vehiculos')

#hist_button = st.button('Construir histograma')

#if hist_button:
    #st.write('Creación de un histograma para los datos de los coches')

    #fig = px.histogram(data, x="odometer")

    #st.plotly_chart(fig, use_container_width=True)