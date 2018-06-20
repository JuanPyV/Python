

palabra = "paracaidas"
n = 3


def separa_guiones(palabra, n):

    palabra1 = list(palabra)
    palabra2 = []

    for x in range(len(palabra1)):
        palabra2.insert(x * n, palabra1[x])

        if (x+1) % n == 0:
            palabra2.insert(x*n+n, "-")
            palabra3 = ''.join(palabra2)

    return palabra3


print(separa_guiones(palabra, n))