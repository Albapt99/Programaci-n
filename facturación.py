cantidad = int(input("Introduzca número de equipajes"))
precio_total = 0
for i in range(cantidad):
    peso = float(input("Introduzca el peso de la maleta"))
    if peso <=10:
        precio = 0
        print("Es equipaje de mano, es gratuito")
    elif peso <=20:
        precio = 20
        print("Debe facturarse, son 20€")
    else:
        precio = 20 + (peso - 20)* 5
        print("Son :", precio, "€")
    precio_total = precio_total + precio
print("El importe total es: ", precio_total)
