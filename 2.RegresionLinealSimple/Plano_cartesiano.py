#Este codigo fue hecho en Google Colab y en el entorno de Github Codespace no ejecuta.
#Se aconseja ejecutarlo en otro entrono que no sea Codespace

import matplotlib.pyplot as plt

# Datos
estatura = [121, 123, 108, 118, 111, 109, 114, 103, 110, 115]
peso = [25, 22, 19, 24, 19, 18, 20, 15, 20, 21]

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.scatter(estatura, peso, color='blue', marker='o')

# Añadir títulos y etiquetas
plt.title('Estatura vs Peso')
plt.xlabel('Estatura (cm)')
plt.ylabel('Peso (kg)')

# Mostrar la cuadrícula
plt.grid()

# Mostrar el gráfico
plt.show()