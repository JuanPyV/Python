listaX = [[1, 5, 8, 9, -11],
          [-1, 5, 7, -8, 6],
          [5, 4, -3, 10, 5]]


# nxn con -1 en cada posicion
def creaMatriz1(n):
    lista1 = []
    for i in range(n):
        lista_1 = []
        for num in range(n):
            lista_1.append(-1)
        lista1.append(lista_1)
    return lista1


print(creaMatriz1(int(input("1.- Dame el numero de renglon: "))))


# nXn con numero representativo
def creaMatriz2(m):
    lista2 = []
    for i in range(m):
        lista_2 = []
        for num2 in range(m):
            lista_2.append(num2)
        lista2.append(lista_2)
    return lista2


print(creaMatriz2(int(input("2.- Dame el numero de renglon: "))))


# nXn con valor correspondienteal renglon
def creaMatriz3(r):
    lista3=[]
    for i in range(r):
        lista_3=[]
        for num in range(r):
            lista_3.append(i)
        lista3.append(lista_3)
    return lista3


print(creaMatriz3(int(input("3.- Dame el numero de renglon: "))))


# nXn con numero consecutivo
def creaMatriz4(c):
    lista4 = []
    for i in range(c):
        lista_4 = []
        for num in range(c):
            lista_4.append(i+1)
            i = c + i
        lista4.append(lista_4)
    return lista4






# cuenta los pares
def cuentaPares(listaP):
    par = 0
    for listap in listaP:
        for elemp in listap:
            if elemp % 2 == 0:
                par = 1 + par
    return par


print("5.- Hay", cuentaPares(listaX), "numeros pares")


# Suma cada valor de localidad
def sumaMatriz (listaS):
    s = 0
    for listas in listaS:
        for elems in listas:
            s = elems + s
    return s


print("6.- La suma es total es:", sumaMatriz(listaX))


# Cuenta cuantos son positivos
def cuentaPositivos(listaPo):
    pos = 0
    for lista in listaPo:
        for elem in lista:
            if elem >= 0:
                pos = 1 + pos
    return pos


print("7.- Hay", cuentaPositivos(listaX), "numeros positivos")


# Convierte a cero los negativos
def cambiaNegativos(listaN):
    for lista in listaN:
        for elem in range(len(lista)):
            if lista[elem] < 0:
                lista[elem] = 0
    return listaN


print("8.-", cambiaNegativos(listaX))


# Cuantas veces se repite x numero
def cuentaRepeticiones(listaR, n):
    rep = 0
    for lista in listaR:
        for elem in lista:
            if elem == n:
                rep = 1 + rep
    return rep


n = int(input("9.- Dame el numero: "))
print("El numero", n, "se repite", cuentaRepeticiones(listaX, n), "veces")


# Busca x en la matriz
def busca(listaB, n):
    for lista in listaB:
        for elem in lista:
            if elem == n:
                return True
    return False


n = int(input("10.- Dame el numero a buscar: "))
print(busca(listaX, n))


# suma los valores mayores a 5
def sumaMayores5(listaS5):
    suma5 = 0
    for lista in listaS5:
        for elem in lista:
            if elem > 5:
                suma5 = elem + suma5
    return suma5


print("11.- La suma de los mayores que 5 es:", sumaMayores5(listaX))


# sustituir todos los ceros  por el resultado de la suma de su número de renglón por su número de columna
def cambiaCeros (listaC):
    for ren in range(len(listaC)):
        for col in range(len(listaC[ren])):
            if listaC[ren][col] == 0:
                listaC[ren][col] = ren + col
    return listaC


print("12.-", cambiaCeros(listaX))
