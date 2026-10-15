maleta = float(input("Introduzca el peso de la maleta"))
if maleta <=10:
    print("Es equipaje de mano, es gratuito")
elif maleta <=20:
    print("Debe facturarse, son 20€")
else:
    importe = 20 + 5 * (maleta - 20)
    print("Son :", importe, "€")