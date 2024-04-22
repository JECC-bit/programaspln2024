import nltk
import matplotlib.pyplot as plt
import os
import PyPDF2

# Leer el nombre del archivo .pdf y validar que exista
salida = False

while not salida:
    pregunta = input("¿Desea ingresar un documento personalizado? (s/n) R = ")
    if pregunta.lower() == "s":
        nombre_archivo = input("Ingresa el nombre del pdf a analizar: ")
        # Validar si el archivo existe en la carpeta del programa
        if os.path.exists(nombre_archivo):
            salida = True
        else:
            print("El archivo '{}' no existe. Por favor, inténtalo de nuevo.".format(nombre_archivo))
    elif pregunta.lower() == "n":
        nombre_archivo = 'cuento.pdf'
        salida = True
    else:
        salida = False

# Cargar el documento .pdf
with open(nombre_archivo, 'rb') as archivo_pdf:
    lector_pdf = PyPDF2.PdfReader(archivo_pdf)
    texto_pagina = ""
    for pagina in range(len(lector_pdf.pages)):
        texto_pagina += lector_pdf.pages[pagina].extract_text()

# Guardar el texto en un documento txt
with open('texto_extraidoPDF.txt', 'w', encoding='utf-8') as archivo:
    archivo.write(texto_pagina)

# Contar el número de palabras y líneas
numero_palabras = len(texto_pagina.split())
numero_lineas = len(texto_pagina.split('\n'))

print("Número de palabras:", numero_palabras)
print("Número de líneas:", numero_lineas)

# Mostrar palabras de 3 o 4 caracteres
palabras_3_4_caracteres = [palabra for palabra in texto_pagina.split() if len(palabra) in [3, 4]]
print("Palabras de 3 o 4 caracteres:", palabras_3_4_caracteres)

# Pedir al usuario que ingrese la palabra a buscar
palabra_buscar = input("Ingresa la palabra que deseas buscar en el texto: ")

# Contar el número de veces que aparece la palabra
numero_apariciones = texto_pagina.lower().count(palabra_buscar.lower())
print("La palabra '{}' aparece {} veces en el texto.".format(palabra_buscar, numero_apariciones))

# Tokenizar el texto y eliminar palabras funcionales
palabras_funcionales = nltk.corpus.stopwords.words("spanish")
tokens = nltk.word_tokenize(texto_pagina, "spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

print("Tokens: ", len(tokens))
print("Tokens limpios: ", len(tokens_limpios))

# Crear un objeto Text de NLTK
texto_nltk = nltk.Text(tokens_limpios)

# Calcular la distribución de frecuencia
distribucion_frecuencia = texto_nltk.vocab()

# Graficar las 40 palabras más comunes
plt.figure(figsize=(10, 6))
texto_nltk.plot(40)
plt.show()