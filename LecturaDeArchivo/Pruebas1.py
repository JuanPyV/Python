try:
    archivo = open("numeros.txt", "r")
    lineas = []
    for linea in archivo:
        lineaP = linea.strip()
        lin = lineaP.split(",")
        lineas.append(lin)

except IOError:
    print("El archivo no existe")


row = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
freeparking = []
freeslot = 0

for letter in lineas:
    for slot in letter:
        print(slot)




