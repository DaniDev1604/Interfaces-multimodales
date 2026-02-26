import streamlit as st
from PIL import Image

st.title("Desarrollado por Dani")

st.header("Pàgina desarrollada como ejemplo de caso para la clase creaciòn de interfaces multimodales")
st.write("Prueba desarrollo de backend y frontend")
image = Image.open("BannerPrueba.jpeg")
st.image(image, caption="Banner")

texto = st.text_input("Escribe algo", "Este es el texto")
st.write("El texto escrito es", texto)
