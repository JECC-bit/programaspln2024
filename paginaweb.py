import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
def calcular_riqueza_lexica(tokens):
    tokens_conjunto = set(tokens)
    palabras_totales = len(tokens)
    palabras_diferentes = len(tokens_conjunto)
    riqueza_lexica = palabras_diferentes / palabras_totales
    return riqueza_lexica
st.title("Análisis de Riqueza Léxica de una Página Web")
url = st.text_input("Ingresa la URL de la página web a analizar:", "https://archiveos.org/pelican/")

if st.button("Analizar"):
    if url:
        respuesta = requests.get(url)


        if respuesta.status_code == 200:
    
            soup = BeautifulSoup(respuesta.content, 'html.parser')

    
            tokens_totales = []

    
            parrafos = soup.find_all('p')

    
            texto_completo = ""
            for paragraph in parrafos:
                texto_completo += paragraph.text + "\n"
                tokens = word_tokenize(paragraph.text, language="english")
                tokens_totales.extend(tokens)

    
            st.subheader("Texto Analizado:")
            st.text(texto_completo)

    
            riqueza_lexica_total = calcular_riqueza_lexica(tokens_totales)
            st.subheader("Resultados del Análisis:")
            st.write("Riqueza léxica total: {:.2f}%".format(riqueza_lexica_total * 100))
        else:
            st.error(f'Error al obtener la página: {respuesta.status_code}')
    else:
        st.error("Por favor, ingresa una URL válida.")
