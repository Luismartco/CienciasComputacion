import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
texto = 'No es lo mismo ser ciego que caminar la vida con ojos vendados'
token1 = word_tokenize(texto)
#token.word_tokenize(texto)
len(texto)
print(token1)
print(len(token1))
texto.split()