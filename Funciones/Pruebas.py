# no necesariamente debe tener el mismo nombre la variable que en la funcion, SOLO EN FUNCIONES"


def multiplos3 (lista):
    cont = 0
    for elem in lista:
        if elem % 3 == 0:
            cont += 1
    return cont

def multiplos3L (lista):
    lista2=[]
    for elem in lista:
        if elem % 3 == 0:
            lista2.append(elem)
    return lista2


lis = [3, 5, 7, 9, 12]
print((multiplos3(lis)))
print((multiplos3L(lis)))