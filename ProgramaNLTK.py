import nltk
import matplotlib.pyplot as plt

with open("..\\PLN\\Programas\\Documentos\\cuento2.txt", "r") as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")

texto_nltk = nltk.Text(tokens)
distribucion = nltk.FreqDist(texto_nltk)
lista_frecuencias = distribucion.most_common()
print(lista_frecuencias)

palabras = [palabra[0] for palabra in lista_frecuencias]
frecuencias = [frecuencia[1] for frecuencia in lista_frecuencias]

# Graficar
plt.figure(figsize=(10, 6))
plt.bar(palabras, frecuencias, color='skyblue')
plt.xlabel('Palabras')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de palabras en el texto')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()