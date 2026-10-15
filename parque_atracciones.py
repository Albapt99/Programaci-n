altura_str = input("¿Cuál es la altura?")
edad_str = input("¿Cuál es la edad?")
altura_str = int(altura_str)
edad_str = int(edad_str)
if altura_str>= 120:
    if edad_str>= 12:
        print("Puedes subir a la atracción")
    else:
        print("Puedes subir con un adulto")
else:
    print("No puedes subir a la atracción")
