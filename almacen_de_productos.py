almacen = []
nuevo = ""
while nuevo!="4":
    print("1. Añadir nuevo producto")
    print("2. Listar todos los productos")
    print("3. Mostrar valor del almacén")
    print("4. Salir del programa")
    nuevo = input("Selecciona una opción (1, 2, 3, 4): ")
    match nuevo:
        case "1":
            almacen.append(nuevo)
            print("Introduzca nombre, cantidad y precio")
        case "2":
            print(almacen)