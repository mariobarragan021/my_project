import pandas as pd
import streamlit as st
import matplotlib as plt
import plotly.express as px


data=pd.read_csv('./vehicles_us.csv')

st.header('Datos de Vehiculos')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para los cilindros de los coches')

    fig = px.histogram(data, x="cylinders")

    st.plotly_chart(fig, use_container_width=True)

dispersion_button = st.button('Construir Diagrama de dispersion')

if dispersion_button:
    st.write('Creación de un diagrama de dispersion para el odometer')

    figure = px.scatter(data, x="odometer" y="price")

    figure.show()