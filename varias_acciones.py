import nltk
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Leer la URL de la página web que deseas analizar
salida = False

while not salida:
    pregunta = input("¿Desea ingresar una URL personalizada? (s/n) R = ")
    if pregunta.lower() == "s":
        liga = input("Ingresa la URL de la página web a analizar: ")
        salida = True
    elif pregunta.lower() == "n":
        liga = 'https://archiveos.org/pelican/'
        salida = True
    else:
        salida = False

# Realizar la solicitud HTTP GET para obtener el contenido de la página
respuesta = requests.get(liga)

# Verificar si la solicitud fue exitosa (código de estado 200)
if respuesta.status_code == 200:
    # Parsear el contenido HTML utilizando BeautifulSoup
    soup = BeautifulSoup(respuesta.content, 'html.parser')
    
    # Obtener solo el texto de los párrafos
    parrafos = soup.find_all('p')
    texto_pagina = ' '.join([parrafo.get_text() for parrafo in parrafos])
    
    # Guardar el texto en un documento txt
    with open('texto_extraido.txt', 'w', encoding='utf-8') as archivo:
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
    palabras_funcionales=nltk.corpus.stopwords.words("spanish")
    tokens=nltk.word_tokenize(texto_pagina,"spanish")
    tokens_limpios=[]
    for token in tokens:
        if token not in palabras_funcionales:
            tokens_limpios.append(token)
            '''print(tokens_limpios)'''

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
    
else:
    print('Error al obtener la página:', respuesta.status_code)
