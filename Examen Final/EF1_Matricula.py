# JUan Pablo Velazco Velasquez

def crear_matriz(n):
    lista = []
# Confirma con coordenadas si son iguales
    for c in range(n):
        lista_1 = []
        for num in range(n):
            if num <= c:
                lista_1.append(1)
            elif num > c:
                lista_1.append(0)

        lista.append(lista_1)
    return lista


def comprobra_matriz(m):
    for c in range(len(m)):
        for num in range(len(m)):
            if num <= c and m[c][num] == 1:
                return True
            elif num > c and m[c][num] == 0:
                return False


def crear_archivo(n):
    matriz = open("Matriz.txt", "w+")
    for row in n:
        matriz.write("\n")
        for num in row:
            matriz.write(str(num) + ",")

    return ("Archivo creado")


def leer_archivo():
    try:
        archivo = open("numeros.txt", "r")
        lineas = []
        for linea in archivo:
            lineaP = linea.strip()
            lin = lineaP.split(",")
            lineas.append(lin)

    except IOError:
        print("El archivo no existe")

    return lineas


#imprime

print(crear_matriz(int(input("Dame el numero de renglon: "))))
m = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
print(comprobra_matriz(m))
lista = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
print(crear_archivo(lista))
print(leer_archivo())
