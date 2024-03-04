import nltk
nltk.download('punkt')

with open("..\\PLN\\Programas\\Documentos\\cuento.txt", "r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print(token)

palabras_total = len(tokens)
print(palabras_total)