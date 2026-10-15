horas = float(input("Introduzca el número de horas que ha permanecido en el aparcamiento"))
if horas <=2:
    importe = 2 * horas
    print("EL importe es: ", importe)
elif horas <=5:
    importe = 1.50 * horas
    importe = float(importe)
    print("EL importe es: ", importe)
else:
    importe = 1 * horas
    print("El importe es: ", importe)