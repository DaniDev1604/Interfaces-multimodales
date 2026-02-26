import streamlit as st
from PIL import Image

st.title("Desarrollado por Dani")

st.header("Pàgina desarrollada como ejemplo de caso para la clase creaciòn de interfaces multimodales")
st.write("Prueba desarrollo de backend y frontend")
image = Image.open("BannerPrueba.jpeg")
st.image(image, caption="Banner")

texto = st.text_input("Escribe algo", "Este es el texto")
st.write("El texto escrito es", texto)

st.subheader("Ahora usemos 2 columnas")
col1,col2 = st.columns(2)

with col1:
  st.subheader("columna 1")
  st.write("mejora la experiencia")  
  resp = st.checkbox("De acuerdo")
  if resp:
    st.write("correcto")    
    
