import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#algoritmo de division de los datos 
data = {
    'duracion': [120, 150, 90, 200, 130, 180, 160, 110], 
    'rating': [4.5, 5.0, 1.2, 3.5,4.2, 4.6,2.8,1.9],
    'genero':['accion', 'drama', 'infantil', 'comedia', 'ciencia ficcion', 'terror', 'romance', 'thriler']
}

datos = pd.DataFrame(data)

#Division en text y entrenamiento
x = datos[['duracion','rating']]
y = datos['genero']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 40)

print("Conjunto de entrenamiento")
print(x_train)
print(y_train)
