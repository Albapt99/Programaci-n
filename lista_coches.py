coches = []
nuevo=""
while nuevo!="FIN":
    nuevo = input("Introduce modelos de coche o escribe FIN para terminar: ")
    if nuevo != "FIN":
        coches.append(nuevo)

print(coches)
print("Programa finalizado")