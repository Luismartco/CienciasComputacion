#importacion de las librerias
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#creacion del set de datos
data = {
    'Estatura': [121, 123, 108, 118, 111, 109, 114, 103, 110, 115],
    'Peso': [25, 22, 19, 24, 19, 18, 20, 15, 20, 21]
}

#Permite manipular datos con pandas
df =pd.DataFrame(data)

#Definir la variable dependiente e independiente
x = df[['Estatura']]
y = df[['Peso']]

#Aplicarle regrecion lineal al modelo
model = LinearRegression()
model.fit(x,y)

# Imprime el coeficiente y la intercepción del modelo
print(f'coeficiente m: {model.coef_[0][0]}') 
print(f'Intercepcion b: {model.intercept_[0]}')

# Define una nueva estatura para predecir el peso
Estatura_nueva = np.array([[200]])
# Predice el peso para la nueva estatura
peso_predecido = model.predict(Estatura_nueva)

# Realiza la predicción
print(f'Peso predicho para estatura 115: {peso_predecido[0][0]}')

print("hola")