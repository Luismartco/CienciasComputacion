#Debe imprimir
# lunes LUNES lunes LUNES
# martes MARTES martes Martes
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
palabra1 = str(input('Digite la palabra 1: '))
palabra2 = str(input('Digite la palabra 2: '))
token1 = word_tokenize(palabra1)
token2 = word_tokenize(palabra2)
print(", ".join(map(str,token1[0:1])),palabra1.upper())
print(", ".join(map(str,token1[0:1])),palabra1.upper())
print(", ".join(map(str,token2[0:1])),palabra2.upper())
print(", ".join(map(str,token2[0:1])),palabra2.capitalize())