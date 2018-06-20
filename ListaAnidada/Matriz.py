import os
import msvcrt

mat1 = [[1, 5], [6, 9]]
mat2 = [[4, 3], [7, 2]]
back = 1


def suma(mat1, mat2):
    suma = []
    for c in range(len(mat1)):
        num = []
        for row in range(len(mat1[c])):
            num.append(mat1[c][row] + mat2[c][row])
        suma.append(num)
    return suma


def resta(mat1, mat2):
    resta = []
    for c in range(len(mat1)):
        num = []
        for row in range(len(mat1[c])):
            num.append(mat1[c][row] - mat2[c][row])
        resta.append(num)
    return resta


def multi_escalar(mat1,n):
    multiesc=[]
    for i in  range(len(mat1)):
        row=[]
        for num in range(len(mat1[i])):
            row.append(mat1[i][num]*n)
        multiesc.append(row)
    return(multiesc)


def multi_matricial(mat1,mat2):
    multimat = []
    for i in range(len(mat1)):
        row = []
        for num in range(len(mat1)):
            valor = 0
            for op in range(len(mat2)):
                valor = valor + mat1[i][op]*mat2[op][num]
            row.append(valor)
        multimat.append(row)
    return(multimat)


while back == 1:
    print("Que Operacion desea efectuar? \n")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion escalar")
    print("4.- Multiplicacion de matrices")
    print("5.- Salir \n")
    n = int(input("Ingrese seleccion: "))

    if n == 1:
        print("-Suma")
        print(suma(mat1, mat2))
    elif n == 2:
        print("-Resta")
        print(resta(mat1, mat2))
    elif n == 3:
        print("-Multiplicacion escalar")
        print(multi_escalar(mat1, float(input("Dame el numero: "))))
    elif n == 4:
        print("-Multiplicacion de matrices")
        print(multi_matricial(mat1, mat2))
    elif n == 5:
        break

    else:
        print("\n **Nel, esa opcion no te la vengo manejando, ingresa una valida** \n")

    print("Presione una tecla para continuar...")
    msvcrt.getch()

    os.system("cls")
