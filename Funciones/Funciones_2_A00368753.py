n = float(input("Dame el numero: "))
lis = ["carro", "perro", "avion", "gato", "casa", "casa", "helicoptero"]


def con_n_letras (lista):
    c = 0
    for elem in lista:

        if len(elem) >= n:
            c += 1

    return c


print((con_n_letras(lis)))