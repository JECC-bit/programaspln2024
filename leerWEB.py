import requests
from bs4 import BeautifulSoup

# URL de la página web que deseas analizar
url = 'https://archiveos.org/pelican/'

# Realizar la solicitud HTTP GET para obtener el contenido de la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsear el contenido HTML utilizando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # En este punto, puedes acceder a elementos específicos de la página utilizando métodos de BeautifulSoup
    # Por ejemplo, para obtener todos los elementos de párrafo (<p>) en la página:
    paragraphs = soup.find_all('p')
    
    # Imprimir el texto de cada párrafo
    for paragraph in paragraphs:
        print(paragraph.text)
else:
    print('Error al obtener la página:', response.status_code)
