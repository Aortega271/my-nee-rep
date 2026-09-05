import streamlit as st
import pandas as pd
import plotly.express as px

st.header("EDA - Cars Dashboard (Plotly + Streamlit)")

# Cargar datos
car_data = pd.read_csv("vehicles_us.csv")
st.write(car_data.columns)
# Botones
col1, col2 = st.columns(2)

with col1:
    build_hist = st.button("Construir histograma")
with col2:
    build_scatter = st.button("Construir dispersión")

# Histograma
if build_hist:
    st.write("Creación de un histograma del dataset (odometer).")
    fig = px.histogram(car_data, x="odometer", nbins=30)
    st.plotly_chart(fig, use_container_width=True)

# Dispersión
if build_scatter:
    st.write("Creación de un gráfico de dispersión (odometer vs price).")
    fig = px.scatter(car_data, x="odometer", y="price", opacity=0.7)
    st.plotly_chart(fig, use_container_width=True)
