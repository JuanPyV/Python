try:
    archivo = open("archivo1.txt", "r")

    for linea in archivo:
        print(linea.rstrip()) # borra el caracter dentro de .rstrip()

    archivo.close()
except IOError:
    print("El archivo no existe")



try:
    arch = open("archivo2.txt", "w", encoding="UTF-8")
    arch.write("Se sobreescribio \n")
    arch.write("todo el archivo \n")
    arch.write("asi mero petarero")

    arch.close()

except:
    print("No se encontro el archivo")



try:
    arch1 = open("archivo1.txt", "r")
    lectura = arch1.read(1)
    while lectura != "":
        print(lectura)
        lectura = arch1.read(1)
except:
    print("El archivo no existe")




try:
    archivo = open("numeros.txt", "r")
    lineas = []
    for linea in archivo:
        lineaP = linea.strip()
        lin = lineaP.split(",")
        lineas.append(lin)

except IOError:
    print("El archivo no existe")

print(lineas)


