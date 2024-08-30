import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
# Frases
frase1 = "En medio de la dificultad se esconde la oportunidad. Albert Einstein"
frase2 = "Solo aquellos que se atreven a fallar mucho pueden lograrlo. –Robert F. Kennedy"
frase3 = "La inteligencia sin ambición es como un pájaro sin sus alas. –Salvador Dalí"
frase4 = "Nunca es demasiado tarde para ser lo que podrías haber sido. –George Eliot"
tokens_frase1 = word_tokenize(frase1)
tokens_frase2 = word_tokenize(frase2)
tokens_frase3 = word_tokenize(frase3)
tokens_frase4 = word_tokenize(frase4)
resultado = {
 "frase1": [tokens_frase1[1], tokens_frase1[3], tokens_frase1[5]], 
 "frase2": [tokens_frase2[1], tokens_frase2[4], tokens_frase2[8]], 
}
print(resultado)
print('no se encuentra la palabra velocidad, en la frase 3')
print('no se encuentra la palabra costosa, en la frase 4')