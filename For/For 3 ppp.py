i = 0
n = int(input("Introduce el numero de valores a sumar: "))

for x in range(n):
    num = float(input("Dame un numero: "))
    i = i + num
print("La suma es: %d" % i)
