
n = 0
suma = 0
c = 0
m = 0

while c < 15:
    n = float(input("Dame la deuda: "))
    suma = n + suma
    c = c + 1

    if n >= 200:
        m = m + 1

print("La deuda total es de : %.2f" % suma)
print(" %d son adeudos mayores a 200" % m)
