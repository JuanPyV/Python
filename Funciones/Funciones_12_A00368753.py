lista = ["hola", "La casa", "reloj", "Gabriel"]

def solo_3(lista):
    for x in range(len(lista)):
        lista[x] = lista[x][:3]
    return lista

print (solo_3(lista))