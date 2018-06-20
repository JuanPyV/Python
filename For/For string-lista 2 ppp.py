p = input("Ingresa una palabra: ")
p2 = input("Ingresa una palabra: ")
c = 0
c2 = 0
v = "aAeEiIoOuU"

for n in p:
    if n in v:
        c = c+1

for n in p2:
    if n in v:
        c2 = c2+1

if c2 > c:
    print("La segunda palabra tiene mas vocales")
    print("Total de vocales: %d" % c2)
elif c2 == c:
    print("Tienen la misma cantidad de vocales")
    print("Total de vocales: %d" % c)
else:
    print("La primera palabra tiene mas vocales")
    print("Total de vocales: %d" % c)




