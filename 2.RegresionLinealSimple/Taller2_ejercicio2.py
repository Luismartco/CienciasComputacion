import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#creacion del set de datos
data = {
    'habitantes': [2500, 2539, 2557, 2561, 2565, 2583, 2587, 2600],
    'demanda': [1009.65, 1076.93, 931.65, 971.41, 1004.20, 973.03, 1041.60, 996.54]
}

df =pd.DataFrame(data)

x = df[['habitantes']]
y = df[['demanda']]

model = LinearRegression()
model.fit(x,y)

########
#Independiente habitantes
#Dependiente demanda de energia
########

# Imprime el coeficiente y la intercepción del modelo
print(f'coeficiente m: {model.coef_[0][0]}')
print(f'Intercepcion b: {model.intercept_[0]}')

hab = int(input("Escriba la cantidad de habitanes estimados por afinia: "))
hab_nuevo = np.array([[hab]])
dem_predecido = model.predict(hab_nuevo)

# Realiza la predicción
print(f'La demanda predicha para la candidad de habitantes {hab_nuevo[0][0]} es : {dem_predecido[0][0]}')

# Gráfica los datos y la línea de regresión
plt.scatter(x, y)
plt.title('Demanda de energia VS cantidad de habitantes')
plt.xlabel('habitantes')
plt.ylabel('demanda')
plt.plot(x, model.predict(x), color = 'yellow')
plt.scatter(hab_nuevo, dem_predecido, color = 'red')
plt.show()