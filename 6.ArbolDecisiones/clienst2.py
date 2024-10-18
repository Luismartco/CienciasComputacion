#Importar las librerias
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#Datos para el arbol
archivo_excel = 'datos.xlsx'
dato = pd.read_excel(archivo_excel)
datos = pd.DataFrame(dato)

#Conversion de los datos
datos['Servicios'] = datos['Servicios'].map({'Internet':0, 'Television':1})

x = datos[['Servicios','HorasAfectacion']]
y = datos['Retiro']

#Entrenamiendo del modelo
model = DecisionTreeClassifier()
model.fit(x,y)

#Predicciones con el modelo
y_pred = model.predict(x)

ClientsWithdrawals = (y_pred == 1).sum()
NotClientsWithdrawals = (y_pred == 0).sum()

#Imprimir el estado de los clientes
print(f'Clientes que se retiraran del servicio: {ClientsWithdrawals}')
print(f'Clientes no que se retiraran del servicio: {NotClientsWithdrawals}')