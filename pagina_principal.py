import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator
import openai
import pyaudio
import wave
import speech_recognition as sr
import pyttsx3
import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
import requests
from bs4 import BeautifulSoup
import os

# Programa de Análisis de Sentimientos
def analisis_sentimientos():
    st.header("Análisis de Sentimientos")
    text = st.text_input("Ingresa un texto para analizar sus sentimientos:")
    
    if text:
        translator = Translator()
        analyzer = SentimentIntensityAnalyzer()
        
        translated = translator.translate(text, src='es', dest='en').text
        sentiment = analyzer.polarity_scores(translated)

        if sentiment['compound'] >= 0.05:
            st.write("Sentimiento detectado: Positivo", sentiment)
        elif sentiment['compound'] <= -0.05:
            st.write("Sentimiento detectado: Negativo", sentiment)
        else:
            st.write("Sentimiento detectado: Neutral", sentiment)

# Programa de ChatGPT
def chat_gpt():
    st.header("Interacción con ChatGPT")
    mensaje = st.text_input("Tu mensaje:")

    if st.button("Enviar"):
        if mensaje:
            respuesta = enviar_solicitud_chat(mensaje)
            st.write("ChatGPT: " + respuesta)

def enviar_solicitud_chat(mensaje, engine='gpt-3.5-turbo-16k', max_tokens=50, temperatura=0.7):
    openai.api_key = ''
    respuesta = openai.Completion.create(
        engine=engine,
        prompt=mensaje,
        max_tokens=max_tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

# Programa de Grabar Audio y Convertirlo a Texto
def grabar_audio_texto():
    st.header("Grabar Audio y Convertir a Texto")
    duracion = st.number_input("Duración de la grabación (segundos):", min_value=1, max_value=60, value=5)

    if st.button("Grabar"):
        nombre_archivo = "grabacion.wav"
        grabar_audio(nombre_archivo, duracion)
        texto_reconocido = convertir_audio_a_texto(nombre_archivo)
        st.write("Texto reconocido:")
        st.write(texto_reconocido)

def grabar_audio(nombre_archivo, duracion):
    formato = pyaudio.paInt16
    canales = 1
    tasa_muestreo = 44100
    tamano_buffer = 1024

    audio = pyaudio.PyAudio()

    stream = audio.open(format=formato, channels=canales, rate=tasa_muestreo, input=True, frames_per_buffer=tamano_buffer)
    frames = []

    for _ in range(0, int(tasa_muestreo / tamano_buffer * duracion)):
        data = stream.read(tamano_buffer)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    archivo_salida = wave.open(nombre_archivo, 'wb')
    archivo_salida.setnchannels(canales)
    archivo_salida.setsampwidth(audio.get_sample_size(formato))
    archivo_salida.setframerate(tasa_muestreo)
    archivo_salida.writeframes(b''.join(frames))
    archivo_salida.close()

def convertir_audio_a_texto(nombre_archivo):
    reconocedor = sr.Recognizer()

    with sr.AudioFile(nombre_archivo) as fuente:
        audio = reconocedor.record(fuente)

    try:
        texto = reconocedor.recognize_google(audio, language='es-ES')
        return texto
    except sr.UnknownValueError:
        return "No se pudo reconocer el audio."
    except sr.RequestError as e:
        return "Error al solicitar resultados al servicio de reconocimiento de voz de Google: {0}".format(e)

# Programa de Convertir Texto a Audio
def convertir_texto_audio():
    st.header("Convertir Texto a Audio")
    texto_reconocido = st.text_input("Ingresa el texto para convertir a audio:")

    if st.button("Convertir"):
        nombre_archivo_salida = "texto_a_voz.wav"
        texto_a_voz(texto_reconocido, nombre_archivo_salida)
        st.audio(nombre_archivo_salida)

def texto_a_voz(texto, nombre_archivo_salida):
    engine = pyttsx3.init()
    engine.save_to_file(texto, nombre_archivo_salida)
    engine.runAndWait()

# Programa de Convertir Archivo .txt a Audio
def convertir_txt_audio():
    st.header("Convertir Archivo .txt a Audio")
    archivo_txt = st.file_uploader("Sube un archivo .txt", type=["txt"])

    if archivo_txt:
        texto = archivo_txt.read().decode("utf-8")
        nombre_archivo_salida = "texto_desde_archivo.wav"
        texto_a_voz(texto, nombre_archivo_salida)
        st.audio(nombre_archivo_salida)

# Programa de Chunky
def chunky():
    st.header("Chunky (Análisis de Frases)")
    text = st.text_input("Ingresa una frase en inglés para ser analizada:")

    if text:
        translator = Translator()
        translated = translator.translate(text, src='es', dest='en').text
        words = word_tokenize(translated)
        tagged = nltk.pos_tag(words)
        etiquetas_pos = nltk.pos_tag(words)

        grammar = """
          NP: {<DT>?<JJ>*<NN|NNS>+}
              {<NNP>+}
        """
        parser = RegexpParser(grammar)
        result = parser.parse(tagged)
        st.write("Análisis de frases:", result)
        ner_chunks = nltk.ne_chunk(etiquetas_pos)
        st.write("Chunks de NER:", ner_chunks)

# Programa de Convertir Voz a Texto y Texto a Audio
def voz_texto_texto_audio():
    st.header("Convertir Voz a Texto y Texto a Audio")
    duracion = st.number_input("Duración de la grabación (segundos):", min_value=1, max_value=60, value=5)

    if st.button("Grabar"):
        nombre_archivo = "voz_reconocida.wav"
        grabar_audio(nombre_archivo, duracion)
        texto_reconocido = convertir_audio_a_texto(nombre_archivo)
        st.write("Texto reconocido:", texto_reconocido)

        if texto_reconocido:
            if st.button("Escuchar"):
                nombre_archivo_salida = "respuesta.wav"
                texto_a_voz(texto_reconocido, nombre_archivo_salida)
                st.audio(nombre_archivo_salida)

# Programa de Análisis de Riqueza Léxica
def riqueza_lexica():
    st.header("Análisis de Riqueza Léxica de una Página Web")
    url = st.text_input("Ingresa la URL de la página web a analizar:")

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

def presentacion_basica_python():
    st.write("Universida de Colima")
    st.write("Ingenieria en Computación Inteligente")
    name = "Jesus Eduardo Ceballos Contreras"
    st.write("Hola ", name)
    st.write("Operacion 1: ", 4*5-6)
    x = 4+7
    y = x-2
    z = x+y
    st.write("X: ", x)
    st.write("Y: ", y)
    st.write("Z: ", z)

def convertir_a_exe():
    programa = st.text_area("Ingresa el código del programa que deseas convertir a .exe:")
    if st.button("Convertir a .exe"):
        with open("programa_a_convertir.py", "w", encoding="utf-8") as archivo:
            archivo.write(programa)
        os.system('pyinstaller --onefile programa_a_convertir.py')
        st.write("Programa convertido a .exe. Revisa la carpeta 'dist'.")

def calcular_riqueza_lexica(tokens):
    tokens_conjunto = set(tokens)
    palabras_totales = len(tokens)
    palabras_diferentes = len(tokens_conjunto)
    riqueza_lexica = palabras_diferentes / palabras_totales
    return riqueza_lexica

# Menú Principal
def main():
    st.title("Menú de Programas")
    menu = ["Análisis de Sentimientos", "ChatGPT", "Grabar Audio y Convertir a Texto", "Convertir Texto a Audio",
            "Convertir Archivo .txt a Audio", "Chunky", "Convertir Voz a Texto y Texto a Audio", "Convertir a .exe", "Análisis de Riqueza Léxica"]
    
    choice = st.sidebar.selectbox("Selecciona una opción", menu)

    if choice == "Análisis de Sentimientos":
        analisis_sentimientos()
    elif choice == "ChatGPT":
        chat_gpt()
    elif choice == "Grabar Audio y Convertir a Texto":
        grabar_audio_texto()
    elif choice == "Convertir Texto a Audio":
        convertir_texto_audio()
    elif choice == "Convertir Archivo .txt a Audio":
        convertir_txt_audio()
    elif choice == "Chunky":
        chunky()
    elif choice == "Convertir Voz a Texto y Texto a Audio":
        voz_texto_texto_audio()
    elif choice == "Convertir a .exe":
        convertir_a_exe()
    elif choice == "Análisis de Riqueza Léxica":
        riqueza_lexica()

if __name__ == '__main__':
    main()
