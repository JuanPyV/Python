
lista = [-40,29,-5,10]


def los_3_menores(lista):
    lista1 = []
    for i in range(3):
        mini = min(lista)
        lista1.append(mini)
        lista.remove(mini)
    lista1 = lista1[:3]
    return lista1


print(los_3_menores(lista))
