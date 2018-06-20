

n = float(input("Dame el numero: "))


def mayoresn (lista):
    c = 0
    for elem in lista:
        if elem > n:
            c += 1
    return c


lis = [3, 5, 7, 9, 12]

print((mayoresn(lis)))