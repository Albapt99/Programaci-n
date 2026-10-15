temperatura_str = input("¿Qué temperatura hace en la habitación?")
estación_str = input("¿En qué estación estás?(P, V, O, I)")
temperatura_str = int(temperatura_str)
if temperatura_str<20:
    if estación_str == "I":
        print("Debes encender la calefacción")
    else:
        print("No es necesario encender nada")
if temperatura_str>25:
    if estación_str == "V":
        print("Debes encender el aire acondicionado")
    else:
        print("No es necesario encender nada")


    