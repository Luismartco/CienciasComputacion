#Tokenizar la cadena pidiendola con un input
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
cadena = str(input('Digite el texto a tokenizar: '))
token2 = word_tokenize(cadena)
print(", ".join(map(str,token2[0:1])),cadena[0:30].upper())