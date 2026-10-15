codigo = input("Introduzca un código con el siguiente formato: (DAM-025)")
print(codigo)
if (codigo [0:3]) == "DAM":
    print("Desarrollo de Aplicaciones Multiplataformas")
elif (codigo [0:3]) == "DAW":
    print("Desarrollo de Aplicaciones Web") 
if (codigo [0:3]) == "ASIR":
    print("Administración de Sistemas Informáticos")
else:
    print("Ciclo desconocido")