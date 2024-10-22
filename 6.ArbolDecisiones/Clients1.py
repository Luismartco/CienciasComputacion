#Importar las librerias
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler

#Datos para el arbol
datos = pd.DataFrame({'nombre':['Cliente1','Cliente2','Cliente3','Cliente4','Cliente5','Cliente6','Cliente7','Cliente8'],
                      'servicios':['Internet', 'Internet','Television','Television','Internet','Internet','Television','Internet'],
                      'horasAfectacion':[8,6,4,2,7,6,5,1],
                      'retiro':[1,1,0,0,1,1,0,0]})
#Conversion de los datos
datos['servicios'] = datos['servicios'].map({'Internet':0, 'Television':1})

x = datos[['servicios','horasAfectacion']]
y = datos['retiro']

scaler = MinMaxScaler()
x = scaler.fit_transform(x)

#Entrenamiendo del modelo
model = DecisionTreeClassifier()
model.fit(x,y)

#Predicciones con el modelo
y_pred = model.predict(x)

ClientsWithdrawals = (y_pred == 1).sum()
NotClientsWithdrawals = (y_pred == 0).sum()

for nombre,pred in zip (datos["nombre"],y_pred):
    estado = "se retira" if pred == 1 else "no se retira"
    print(f'{nombre}: {estado}')

#Imprimir el estado de los clientes
print(f'Clientes que se retiraran del servicio: {ClientsWithdrawals}')
print(f'Clientes no que se retiraran del servicio: {NotClientsWithdrawals}')