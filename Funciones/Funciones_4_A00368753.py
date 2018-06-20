
lis = [1, -2, 3, -4, 5, -6, 7, -8]


def duplica (lista):

    for n in range(len(lista)):
        lista[n] *= 2

    return lista

print(duplica(lis))
