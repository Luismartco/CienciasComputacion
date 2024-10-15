import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

data = {
      'Edad':[25,48,55,20,30,65,44,70,21],
      'Ingresos':[600,400,150,300,90,120,218,200,500],
      'Compras':[2,3,6,1,7,4,7,3,2],
      'Descuento':['si','no','si','si','no','no','si','si', 'no']
}
dataf = pd.DataFrame(data)

dataf['Descuento'] = dataf['Descuento'].map({'si':1, 'no':0})


X = dataf[['Edad', 'Ingresos', 'Compras']]
Y = dataf[['Descuento']]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, random_state = 35)

model = DecisionTreeClassifier()
model.fit(X_train,Y_train)

prediction = model.predict(X_test)

print(prediction)
plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=X.columns, class_names=['No', 'Si'], filled=True)
plt.title("Mi primer diagrama de árbol de decisión")
plt.show()