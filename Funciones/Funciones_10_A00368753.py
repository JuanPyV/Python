import random

n = int(input("cuantas veces tirar el dado: "))


def tirada (n):
    acum = 0
    a = 1
    b = 6

    for x in range(n):

        c = random.randint(a, b)
        acum = acum + c

    return acum


print(tirada(n))
