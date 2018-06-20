
n = float(input("cuantas veces: "))

mult = 1
contador = 1

while contador <= n:

    mult = 2 * contador * mult
    contador = contador + 1

print(mult)
