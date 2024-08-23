import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Descargas necesarias
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

def analizador_sentimientos():
    print("¡Bienvenido al analizador de sentimientos!")
    print("Escribe una frase y te diré si es positiva, negativa o neutral.")
    print("Escribe 'salir' para terminar.")

    # Inicializar el analizador de sentimientos
    sia = SentimentIntensityAnalyzer()
    stop_words = set(stopwords.words('spanish'))

    while True:
        frase = input("Ingresa una frase: ")

        if frase.lower() == 'salir':
            print("¡Hasta luego!")
            break

        # Tokenizar la frase
        palabras = word_tokenize(frase)

        # Filtrar las palabras vacías
        palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words]

        # Analizar el sentimiento
        puntaje = sia.polarity_scores(frase)

        # Determinar el sentimiento
        if puntaje['compound'] >= 0.05:
            sentimiento = "positivo"
        elif puntaje['compound'] <= -0.05:
            sentimiento = "negativo"
        else:
            sentimiento = "neutral"

        print(f"Palabras tokenizadas (sin palabras vacías): {palabras_filtradas}")
        print(f"Puntaje de sentimiento: {puntaje}")
        print(f"Sentimiento general: {sentimiento}")

if __name__ == "__main__":
    analizador_sentimientos()
