import pandas as pd

pacientes = 'Pacientes2.csv'
dato = pd.read_csv(pacientes)
datos = pd.DataFrame(dato)

datos.info()

##Terminar despues :3