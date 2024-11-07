print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este programa comprueba si tu nombre y apellido son correctos  ") #imprime el nombre y titulos
print("")#imprime espacio en blanco 

# Definir las variables de nombre y apellido
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")

# Comprobar el nombre y el apellido
if nombre == "Luis Angel":
    if apellido == "Martinez Tagle ":
        print("Nombre y apellido correctos.")
    else:
        print("Apellido incorrecto.")
else:
    print("Usuario desconocido.")
