from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator

translator = Translator()
analyzer = SentimentIntensityAnalyzer()

text = input("Ingresa un texto para analizar sus sentimientos: ")
translated = translator.translate(text, src='es', dest='en').text
sentiment = analyzer.polarity_scores(translated)

# Determinar el sentimiento general basado en el valor compound
if sentiment['compound'] >= 0.05:
    print("\nSentimiento detectado: Positive\n", sentiment)
elif sentiment['compound'] <= -0.05:
    print("\nSentimiento detectado: Negative\n", sentiment)
else:
    print("\nSentimiento detectado: Neutral\n", sentiment)