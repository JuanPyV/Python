p = input("Ingresa una palabra: ")
v = input("Ingresa otra palabra: ")


def coinciden (p):

    lista = ""
    i = 0
    for n in p:
        if n == v[i]:
            lista = lista + n
            i = i+1
    return lista


print(coinciden(p))
