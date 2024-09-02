import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#creacion del set de datos
data = {
    'rendimiento': [1.2, 1.8, 3.0, 3.5],
    'satisfaccion': [2, 5, 8, 10]
}

df =pd.DataFrame(data)

x = df[['rendimiento']]
y = df[['satisfaccion']]

model = LinearRegression()
model.fit(x,y)

########
#Independiente rendimiento
#Dependiente satisfaccion
########

# Imprime el coeficiente y la intercepción del modelo
print(f'coeficiente m: {model.coef_[0][0]}')
print(f'Intercepcion b: {model.intercept_[0]}')

ren = float(input("Escriba el valor del rendimiento del procesador en GHZ: "))
ren_nuevo = np.array([[ren]])
sat_predecido = model.predict(ren_nuevo)

# Realiza la predicción
print(f'satisfaccion predicho para el rendimiento la {ren_nuevo[0][0]} es : {sat_predecido[0][0]}')

# Gráfica los datos y la línea de regresión
plt.scatter(x, y)
plt.title('rendimiento VS satisfaccion')
plt.xlabel('rendimiento')
plt.ylabel('satisfaccion')
plt.plot(x, model.predict(x), color = 'yellow')
plt.scatter(ren_nuevo, sat_predecido, color = 'red')
plt.show()