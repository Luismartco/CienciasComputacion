import pandas as pd
from sklearn.linear_model import _linealRegression

from sklearn.linear_model import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

archivo = 'datos_viviendas.xlsx'
df=pd.read_excel(archivo)
print(df.head)

x = df[['TAMANO','HABITACIONES','ANTIGUEDAD']]
y = ['PRECIO']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state = 40)