nota = input("Introduce nota numérica:")
nota= float(nota) #conversion a numero
print(nota)
nota_str = input("cual es la nota")
nota = int(nota_str)
if nota<6:
    if nota<5:
        if nota<3:
           print("Muy deficiente")
        else:
            print("Insuficiente")
    else:
        print("Suficiente")
else:
  if nota<7:
      print("bien")
  else:
      if nota<9:
          print("notable")
      else:
          print("sobresaliente")
print ("final del programa")
          