import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

file_path = 'jugadores_seleccion.xlsx' 
data = pd.read_excel(file_path)

le = LabelEncoder()
data['Posición'] = le.fit_transform(data['Posición'])

X = data.drop(columns=['Jugador', 'Titular (Etiqueta)'])
y = data['Titular (Etiqueta)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

probabilidades_all = knn.predict_proba(X) 

data['Probabilidad de ser titular'] = probabilidades_all[:, 1] 

jugadores_seleccionados = data[['Jugador', 'Probabilidad de ser titular']].sort_values(by='Probabilidad de ser titular', ascending=False)

jugadores_titulares = jugadores_seleccionados.head(11)

print(jugadores_titulares)
