
l = input("Dame la letra: ")
lis = ["alo", "hola", "carro", "auto", "avion", "arbol", "perro"]


def empieza_con(lista):
    c = 0
    for x in lista:
        p = x[0]
        if p == l:
            c += 1
    return c


print((empieza_con(lis)))
