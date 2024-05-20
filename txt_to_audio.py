import pyaudio
import wave
import speech_recognition as sr
import pyttsx3



def texto_a_voz(texto, nombre_archivo_salida):
    engine = pyttsx3.init()
    engine.save_to_file(texto, nombre_archivo_salida)
    engine.runAndWait()

def leer_archivo_txt(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            return texto
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no fue encontrado.")
        return ""
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {ruta_archivo}: {e}")
        return ""

# Leer texto desde un archivo .txt
ruta_archivo_txt = "Pruebagit.txt"
texto_desde_archivo = leer_archivo_txt(ruta_archivo_txt)

# Reproducir el texto del archivo .txt utilizando la voz de Google
if texto_desde_archivo:
    texto_a_voz(texto_desde_archivo, "texto_desde_archivo.wav")
