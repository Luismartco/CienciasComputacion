import numpy as np
from sklearn.preprocessing import StandardScaler

#datos para normalizar
conjunt = np.array([[10,0],[15,2],[25,10],[30,15]])

scaler = StandardScaler()

escalaDatos = scaler.fit_transform(conjunt)

print(escalaDatos)
