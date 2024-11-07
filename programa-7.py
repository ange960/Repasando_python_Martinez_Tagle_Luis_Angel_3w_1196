print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este programa  imprime  suma el valor de todos los números pares desde el 2 (inclusive) hasta el 100 ") #imprime el nombre y titulos
print("")#imprime espacio en blancos


# Inicializar la variable para almacenar la suma
suma_pares = 0

# Usar un rango para iterar sobre los números pares desde 2 hasta 100 (inclusive)
for numero in range(2, 101, 2):  # El tercer parámetro '2' hace que el rango solo considere números pares
    suma_pares += numero

# Imprimir el resultado
print("La suma de los números pares desde 2 hasta 100 es:", suma_pares)
