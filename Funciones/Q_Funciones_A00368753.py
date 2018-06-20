# Juan Pablo Velazco Velasquez A00368753
import math

c = 0

x = float(input("Dame el numero: "))
n = float(input("Hasta que potencia: "))


def progresion (x, n):
    acum = 1
    while c < n:
        if n == 0:
            return acum
        else:
            acum = math.pow(x, n) + acum
            acum += 1
    return acum


print(progresion(x,n))



