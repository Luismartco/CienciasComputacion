import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


Archivo = 'datos_viviendas.xlsx'
df = pd.read_excel(Archivo)
print(df.head)

X = df[['TAMANO', 'HABITACIONES', 'ANTIGUEDAD']]
Y = df[['PRECIO']]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2 , random_state = 40)
# entrenamiento y un test a X y a Y con respecto a sus variables. Y solo se tomará el 20% para el test.

model = LinearRegression()

#Entrenamiento
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

mse = mean_absolute_error(y_test, y_pred)
r2= r2_score(y_test, y_pred)

Valores_nuevos = [[110, 2, 20 ]]
prediccion = model.predict (Valores_nuevos)
print(prediccion)