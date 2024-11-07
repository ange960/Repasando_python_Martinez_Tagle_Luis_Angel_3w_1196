print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 este programa comprueba que rango tienes por la calificacion que sacaste ") #imprime el nombre y titulos
print("")#imprime espacio en blanco 

# Definir la nota en una variable
nota = float(input("Introduce tu nota: "))  # Usamos float por si la nota tiene decimales

# Comprobar el rango de la nota e imprimir el equivalente correspondiente
if 0 <= nota < 5:
    print("orrible")
elif 5 <= nota < 6:
    print("le podrias echar mas ganas ")
elif 6 <= nota < 7:
    print("lo hiciste bien pero puedes mejorar")
elif 7 <= nota < 9:
    print("excelente ")
elif 9 <= nota <= 10:
    print("maraviloso eres un excelente alumno ")
else:
    print("NOTA NO VÁLIDA")
