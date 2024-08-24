#Se definen los array
estatura = [121, 123, 108, 118, 111, 109, 114, 103, 110, 115]
peso = [25, 22, 19, 24, 19, 18, 20, 15, 20, 21]

#Se hace la sumatoria de todos los datos del array
suma_peso = sum(estatura)
suma_estatura = sum(peso)

#Se define Ygorro y Xgorro
gsuma_peso = sum(peso)/10
gsuma_estatura = sum(estatura)/10

#Imprimimos los datos para corroborar 
print("Gorro suma de estatura:", gsuma_estatura)
print("Gorro suma de peso:", gsuma_peso)
print("Suma de estatura:", suma_estatura)
print("Suma de peso:", suma_peso)

#########################################
#Hallamos las variables de b
#########################################

#Hallamos la cantidad de datos
cantidad_datos = len(estatura)

#Imprimimos la cantidad de datos
print("Cantidad de datos en estatura:", cantidad_datos)

#Se halla x*y en cada posicion
resultado = [e * p for e, p in zip(estatura, peso)]

#Sumamos los datos obtenidos
suma_resultado = sum(resultado)

#Imprimomos la sumatoria de los datos de x*y
print("Suma de estatura:", suma_resultado)

#Elebamos al cuadrado la estatura (y)
estatura2 = [e ** 2 for e in estatura]

#Sumamos las estaturas al cuadrado
suma_estatura2 = sum(estatura2)

#Imprimimos las estatuas al cuadrado
print("Suma de estatura:", suma_estatura2)

#########################################
#Hallamos b
#########################################

#Reemplazamos los datos para hallar b
b = ((cantidad_datos*suma_resultado) - (suma_estatura*suma_peso))/((cantidad_datos*suma_estatura2) - (suma_peso**2))

#Imprimimos b
print("Valor de b:", b)

#########################################
#Hallamos a
#########################################

#Reemplazamos los datos para hallar a
a = gsuma_peso - (b*gsuma_estatura)

#Imrimimos a
print("Valor de a:", a)

#########################################
#Hallamos y
#########################################

#Reemplazamos a y b en la ecuacion de la recta y le damos un valor en x
y = a+(b*100)

#Imprimimos y
print(y)

#Reemplazamos a y b en la ecuacion de la recta y le damos un valor en x
y = a+(b*150)

#Imprimimos y
print(y)