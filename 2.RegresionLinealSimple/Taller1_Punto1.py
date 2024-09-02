#Importar pandas
import pandas as pd

# Cargar adultos
adultos = pd.read_excel('Adults.xlsx')

# Cargar Niños 
niños = pd.read_excel('Childrens.xlsx')

# Cargar Ancianos
ancianos = pd.read_excel('Older.xlsx')

# Mostrar la info de los dataset
print(adultos)
print(niños)
print(ancianos)