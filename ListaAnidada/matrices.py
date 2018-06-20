#Mayra Patricia Guajardo Palomera A01634475

#1 creaMatriz1

def creaMatriz1(n):
    listaA=[]
    for i in range(n):
        lista_int=[]
        for num in range(n):
            lista_int.append(-1)
        listaA.append(lista_int)
    return listaA

#2 creaMatriz2
def creaMatriz2(n):
    listaA=[]
    for i in range(n):
        lista_int = []
        for num in range(n):
            lista_int.append(num)
        listaA.append(lista_int)
    return listaA

#3 creaMatriz3
def creaMatriz3(n):
    listaA=[]
    for i in range(n):
        lista_int=[]
        for num in range(n):
            lista_int.append(i)
        listaA.append(lista_int)
    return listaA

#4 creaMatriz4
def creaMatriz4(n):
    listaA=[]
    for i in range(n):
        lista_int=[]
        for num in range(n):
            lista_int.append(i+1)
            i+=n
        listaA.append(lista_int)
    return listaA
print(creaMatriz4(5))

#5 cuentaPares
def cuentaPares(listaA):
    pares=0
    for lista in listaA:
        for elem in lista:
            if elem%2==0:
                pares+=1
    return pares

#6 sumaMatriz
def sumaMatriz (listaA):
    suma=0
    for lista in listaA:
        for elem in lista:
            suma+=elem
    return suma

#7 cuentaPositivos
def cuentaPositivos(listaA):
    pos=0
    for lista in listaA:
        for elem in lista:
            if elem>=0:
                pos+=1
    return pos

#8 cambiaNegativos
def cambiaNegativos(listaA):
    for lista in listaA:
        for elem in range(len(lista)):
            if lista[elem]<0:
                lista[elem]=0

#9 cuentaRepeticiones
def cuentaRepeticiones(listaA,n):
    repetido=0
    for lista in listaA:
        for elem in lista:
            if elem==n:
                repetido+=1
    return repetido

#10 busca
def busca(listaA,n):
    for lista in listaA:
        for elem in lista:
            if elem in lista:
                return True
    return False

#11 sumaMayores5
def sumaMayores5(listaA):
    suma=0
    for lista in listaA:
        for elem in lista:
            if elem>5:
                suma+=elem
    return suma

#12 cambiaCeros
def cambiaCeros (listaA):
    for ren in range(len(listaA)):
        for col in range(len(listaA[ren])):
            if listaA[ren][col]==0:
                listaA[ren][col]=ren+col

#ejemplo para creaMatriz4
def ejemplo (n):
    valor=1
    listaA=[]
    for i in range(n):
        lista_int=[]
        for num in range(n):
            lista_int.append(valor)
            valor+=1
        listaA.append(lista_int)
    return listaA
print(ejemplo(5))
