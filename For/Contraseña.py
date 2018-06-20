print("Krnal, esto sirve para hacerte una contra bien chida")
print("Para esto ocupamos 5 palabras de 3 a 9 letras de lo que quieras")

p1 = input("Escribe la primera I : ")
if len(p1) < 3 or len(p1) > 9:
    print("We, dije que debe tener de 3 a 9 letras")
    p1 = input("Escribe la primera I : ")

p2 = input("Escribe la segunda II : ")
if len(p2) < 3 or len(p2) > 9:
    print("We, dije que debe tener de 3 a 9 letras")
    p2 = input("Escribe la segunda II : ")

p3 = input("Escribe la tercera III : ")
if len(p3) < 3 or len(p3) > 9:
    print("We, dije que debe tener de 3 a 9 letras")
    p3 = input("Escribe la tercera III : ")

p4 = input("Escribe la cuarta IV : ")
if len(p4) < 3 or len(p4) > 9:
    print("We, dije que debe tener de 3 a 9 letras")
    p4 = input("Escribe la cuarta IV : ")

p5 = input("Escribe la quinta V : ")
if len(p5) < 3 or len(p5) > 9:
    print("We, dije que debe tener de 3 a 9 letras")
    p5 = input("Escribe la quinta V : ")

pt = p3 + p5 + p2 + p1 + p4

print(pt)


