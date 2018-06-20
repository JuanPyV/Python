palabra = list("murcielago")

def invierte(palabra):

    palabra2 = []
    for letra2 in range(len(palabra)):

        palabra2.append(palabra[-letra2-1])

    return palabra2

print(invierte(palabra))