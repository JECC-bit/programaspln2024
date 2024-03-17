import nltk

def concordancia(word, tokens):

    txtUsingNltk = nltk.Text(tokens)
    txtUsingNltk.concordance(word)
    return txtUsingNltk

def similares(word, tokens):
    txtUsingNltk2 = nltk.Text(tokens)
    txtUsingNltk2.similar(word)
    return txtUsingNltk2

carpeta_nombre="..\\PLN\\Programas\\Documentos\\"
archivo_nombre="cuento.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")

#LLamado de funciones
result_concordance = concordancia("faro", tokens)
result_similares = similares("farero", tokens)
print("\n\n", result_concordance)
print("\n\n", result_similares)




