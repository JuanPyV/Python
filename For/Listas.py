
lcadena = list("Alooo polecia")
vocalessinaA = "eEiIoOuU"
for indice in range(len(lcadena)):
    if lcadena[indice] in vocalessinaA:
        lcadena[indice] = "i"

cadena2 = "".join(lcadena)
print(cadena2)

