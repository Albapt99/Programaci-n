planta = input("Introduzca la planta actual")
destino = input("Introduzca planta a la que desee ir")
if destino > planta:
    print("Subiendo")
elif destino < planta:
    print("Bajando")
else:
    print("Ya estás en esa planta")