palabra = "murcielago"


def vocales_mayuscula(palabra):

    cambiada = ""

    for letra2 in palabra:

        if letra2 == "a":
            cambiada = cambiada + "A"
        elif letra2 == "e":
            cambiada = cambiada + "E"
        elif letra2 == "i":
            cambiada = cambiada + "I"
        elif letra2 == "o":
            cambiada = cambiada + "O"
        elif letra2 == "u":
            cambiada = cambiada + "U"
        else:
            cambiada = cambiada + letra2

    return cambiada


print(vocales_mayuscula(palabra))