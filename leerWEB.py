import nltk
import requests
from bs4 import BeautifulSoup

# Funcion para calcular la riqueza léxica
def calcular_riqueza_lexica(tokens):
    tokens_conjunto = set(tokens)
    palabras_totales = len(tokens)
    palabras_diferentes = len(tokens_conjunto)
    riqueza_lexica = palabras_diferentes / palabras_totales
    return riqueza_lexica

# URL de la página web que deseas analizar
liga = input("Ingresa la URL de la página web a analizar: ")

# Realizar la solicitud HTTP GET para obtener el contenido de la página
respuesta = requests.get(liga)

# Verificar si la solicitud fue exitosa (código de estado 200)
if respuesta.status_code == 200:
    # Parsear el contenido HTML utilizando BeautifulSoup
    soup = BeautifulSoup(respuesta.content, 'html.parser')
    
    # Inicializar una lista para almacenar todos los tokens
    tokens_totales = []
    
    # En este punto, puedes acceder a elementos específicos de la página utilizando métodos de BeautifulSoup
    # Por ejemplo, para obtener todos los elementos de párrafo (<p>) en la página:
    parrafos = soup.find_all('p')
    
    # Imprimir el texto de cada párrafo y calcular los tokens para cada uno
    for paragraph in parrafos:
        print(paragraph.text)
        tokens = nltk.word_tokenize(paragraph.text, language="english")
        tokens_totales.extend(tokens)  
    
    # Calcular la riqueza léxica utilizando la lista total de tokens
    riqueza_lexica_total = calcular_riqueza_lexica(tokens_totales)
    print("\n\n Riqueza léxica total: {:.2f}%".format(riqueza_lexica_total * 100))
else:
    print('Error al obtener la página:', respuesta.status_code)
