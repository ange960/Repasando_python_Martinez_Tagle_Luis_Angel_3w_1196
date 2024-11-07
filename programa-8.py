print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este programa Imprime la tabla de multiplicar de un número almacenado en una variable utilizando rangos.   ") #imprime el nombre y titulos
print("")#imprime espacio en blancos

# Definir el número para el cual se quiere la tabla de multiplicar
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Generar la tabla de multiplicar utilizando un rango
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):  # Desde 1 hasta 10
    print(f"{numero} * {i} = {numero * i}")
