#Triangulos
lado1 = input("Introduce lado 1: ")
lado2 = input("Introduce lado 2: ")
lado3 = input("Introduce lado 3: ")
lado1 = int(lado1)
lado2 = int(lado2)
lado3 = int(lado3)

if lado1==lado2 and lado2==lado3:
    print("Triángulo equilátero")
else:
    if lado1==lado2 or lado2==lado3 or lado1==lado3:
        print("Triángulo isósceles")
    else:
        if lado1!=lado2!=lado3:
            print("Triángulo escaleno")

