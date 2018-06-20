cadena2 = "aereo"


def locura(cadena2):

    cambiada = ""

    for letra2 in cadena2:

        if letra2 == "a":
            cambiada = cambiada + "4"
        elif letra2 == "o":
            cambiada = cambiada + "h"
        elif letra2 == "e":
            cambiada = cambiada + "3"
        else:
            cambiada = cambiada + letra2

    return cambiada


print(locura(cadena2))