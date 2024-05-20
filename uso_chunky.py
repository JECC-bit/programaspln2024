import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from googletrans import Translator

# Texto de entrada
text = "NLTK is a Python library for natural language processing."
translator = Translator()
translated = translator.translate(text, src='es', dest='en').text

# Tokenización de palabras
words = word_tokenize(translated)

# Etiquetado de partes del discurso
tagged = nltk.pos_tag(words)
etiquetas_pos = nltk.pos_tag(words)

# Definición de una gramática más completa para frases nominales
grammar = """
  NP: {<DT>?<JJ>*<NN|NNS>+}  # Determinante opcional, adjetivos, seguido de uno o más sustantivos (singular/plural)
      {<NNP>+}               # Uno o más sustantivos propios
"""

# Crear un analizador utilizando la gramática definida
parser = RegexpParser(grammar)

# Aplicar el analizador al texto etiquetado
result = parser.parse(tagged)

# Imprimir el resultado
print(result)

nltk.ne_chunk(etiquetas_pos)
from nltk import ne_chunk, pos_tag, word_tokenize
#text = "Barack Obama was born in Hawaii."
text = input("Ingresa una frase en inglés para ser analizada: ")
translated = translator.translate(text, src='es', dest='en').text
tokens = word_tokenize(translated)
pos_tags = pos_tag(tokens)
ner_chunks = ne_chunk(pos_tags)
print("\n\n")
print(ner_chunks)
