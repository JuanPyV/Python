lista = [1, 2, 3, 4, 5, 6]
x = 10


def busqueda_binaria (lista, x):

    izq = 0
    der = len(lista) - 1

    while izq <= der:

        mitad = (izq + der) // 2

        if lista[mitad] == x:
            return mitad

        elif lista[mitad] > x:
            der = mitad - 1

        else:
            izq = mitad + 1

    return -1


print(busqueda_binaria(lista, x))
