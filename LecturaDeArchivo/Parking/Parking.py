import random


def simulacion():
    x = 0
    y = 1
    l = ""
    for n in range(10):
        if n != 0:
            l = l + "\n"
        for c in range(15):
            a = str(random.randint(x, y)) + ","
            l = l + a

    parkeadero = open("Estacionamiento.txt", "w+")
    parkeadero.write(l)


def lee_archivo():
    try:
        parkeadero = open("Estacionamiento.txt", "r")
        lineas = []
        for linea in parkeadero:
            lineaP = linea.strip()
            lineaP = lineaP.strip(",")
            lin = lineaP.split(",")
            lineas.append(lin)

    except IOError:
        print("El archivo no existe")
    return lineas


def escribe_vacios(lineas):
    row = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

    arch = open("Vacios.txt", "w+")
    for letter in range(len(lineas)):
        for slot in range(len(lineas[letter])):
            if lineas[letter][slot] == "0":
                d = str(slot + 1)
                lineas[letter][slot] = row[letter] + d
                arch.write(lineas[letter][slot])
                arch.write(", ")


simulacion()
print("Datos recibidos del sistema de sensores...")
lee_archivo()
print("Lectura del archivo completeda...")
escribe_vacios(lee_archivo())
print("Escritura del archivo vacios.txt completada...")


