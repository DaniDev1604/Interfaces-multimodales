import streamlit as st
from PIL import Image

st.title("Desarrollado por Dani")

st.header("Página desarrollada como ejemplo de caso para la clase creación de interfaces multimodales")
st.write("Prueba desarrollo de backend y frontend")

try:
    image = Image.open("BannerPrueba.jpeg")
    st.image(image, caption="Banner")
except:
    st.warning("No se encontró la imagen 'BannerPrueba.jpeg'. Verifica el nombre del archivo.")

texto = st.text_input("Escribe algo", "Este es el texto")
st.write("El texto escrito es:", texto)

st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Columna 1")
    st.write("Mejora la experiencia")  
    resp = st.checkbox("De acuerdo")
    if resp:
        st.write("Correcto")    

with col2:
    st.subheader("Columna 2")
    modo = st.radio("Modalidad principal en la interfaz", ("Visual", "Auditiva", "Táctil"))
    
    if modo == "Visual":
        st.write("Vista fundamental para la interfaz")    
    elif modo == "Auditiva": # Usar elif es más eficiente
        st.write("Audio fundamental para la interfaz") 
    elif modo == "Táctil":
        st.write("Tacto fundamental para la interfaz")
