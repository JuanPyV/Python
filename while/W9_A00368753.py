
x = int(input("Cuantos numeros: "))

p, n, c, i = 0, 0, 0, 0

while i < x:
    num = int(input("Dame el numero: "))

    if num > 0:
        p = p + 1

    elif num < 0:
        n = n + 1

    else:
        c = c + 1

    i = i + 1

print("Hay %d numeros positivos" % p)
print("Hay %d numeros negativos" % n)
print("Hay %d ceros" % c)




