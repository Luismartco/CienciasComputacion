#Importar las librerias
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#Datos para el arbol
datos = pd.DataFrame({'Servicios':['Internet', 'Internet','Television','Television','Internet','Internet','Television','Internet'],
                      'HorasAfectacion':[8,6,4,2,7,6,5,1],
                      'Retiro':[1,1,0,0,1,1,0,0]})
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