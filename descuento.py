importe = float(input("Introduzca importe"))
cliente = input("¿Es cliente habitual (S, N)?")
if cliente == "S" or importe > 100:
    descuento = importe * 0.10
    importe_total = importe - descuento
    print("El importe total es: ", importe_total)
else:
    print("El importe total es: ", importe)
