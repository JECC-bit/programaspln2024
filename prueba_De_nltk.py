import nltk
nltk.download('punkt')

with open("..\\PLN\\Programas\\Documentos\\cuento.txt", "r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

tokens_conjunto = set(tokens)

palabras_total = len(tokens)
palabras_diferentes = len(tokens_conjunto)
riqueza = palabras_diferentes/palabras_total
print(riqueza)