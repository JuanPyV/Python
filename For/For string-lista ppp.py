p = input("Ingresa una palabra: ")
v = "aAeEiIoOuU"
c = 0

for n in p:
    if n in v:
        c = c+1

print("Total de vocales: %d" % c)


