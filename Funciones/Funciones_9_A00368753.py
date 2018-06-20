
lista1 = list("murcielago")
lista2 = list("avioneta")


def combina_listas(lista1, lista2):
    lista = []

    if len(lista1) > len(lista2):
        tamañomenor = lista2
        tamañomayor = lista1
    else:
        tamañomenor = lista1
        tamañomayor = lista2

    for x in range(len(tamañomenor)):

        lista.append(lista1[x])
        lista.append(lista2[x])
        lista3 = lista + tamañomayor[(x + 1):]
        lista4 = "".join(lista3)

    return lista4


print(combina_listas(lista1, lista2))

