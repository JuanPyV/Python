def lee_archivos():
    try:
        archivo = open("archivo1.txt", "r")
        lista_arch = []
        for linea in archivo:
            lineaP = linea.rstrip()
            l = lineaP.split(",")
            lista_arch.append(l)
        archivo.close()
    except IOError:
        print("No se puede abrir el archivo")

    return lista_arch


# a
def calif_final(listaCalif):
    try:
        archivo = open("archivo1.txt", "w", encoding="UTF-8")
        for n in range(len(listaCalif)):
            final = 0
            for num in range(len(listaCalif[n])):
                if num == 1:
                    final = final + int(listaCalif[n][1]) * .25
                elif num == 2:
                    final = final + int(listaCalif[n][2]) * .45
                elif num == 3:
                    final = final + int(listaCalif[n][3]) * .30
            listaCalif[n].append(final)
            if n != len(listaCalif):
                archivo.write(listaCalif[n][0] + "," + listaCalif[n][1] + "," + listaCalif[n][2]
                           + "," + listaCalif[n][3] + "," + str("%.2f" % listaCalif[n][4]) + "\n")
            else:
                archivo.write(listaCalif[n][0] + "," + listaCalif[n][1] + "," + listaCalif[n][2]
                           + "," + listaCalif[n][3] + "," + str("%.2f" % listaCalif[n][4]))


    except IOError:
        print("No se puede abrir el archivo")

    return listaCalif


# (b
def promedio_parcial(cali, parci):
    calif = 0
    cont = 0
    for nota in cali:
        calif += int(nota[parci])
        cont += 1
        promedio = calif / cont
    return "\n" + "El promedio grupal del parcial " + str(parci) + " es %.2f" % promedio


# c)
def despliega_finales(calificacion):
    for cali in calificacion:
        print("La calificacion final de " + cali[0] + " es: " + str(cali[4]))


def validacion(lista):
    if len(lista[0]) != 5:
        print("El archivo NO tiene las calificaciones finales")
        print("El archivo ya se guardo con las calificaciones finales..." + "\n")
        Cal_Final = calif_final(lista)
        despliega_finales(Cal_Final)
    else:
        print("El archivo SI tiene las calificaciones finales")
        despliega_finales(lee_archivos())


parci = int(input("¿De que parcial quieres el promedio? : "))
validacion(lee_archivos())
promedio = promedio_parcial(lee_archivos(), parci)
print(promedio)
