import math
import os
import msvcrt

# Autor: Juan Pablo Velazco Velasquez
# Programa para calcular area del circulo, cuadrado, triangulo, rectangulo y rombo

def triangulo (b, h):
    a = (b*h)/2
    print("\n El area del tiangulo es: %.2f \n" % a)
def cuadrado (l):
    a = l*l
    print("\n El area del cuadrado es: %.2f \n" % a)
def rectangulo (b, h):
    a = b*h
    print("\n El area del rectangulo es: %.2f \n" % a)
def rombo (D, d):
    a = D*d
    print("\n El area del rombo es: %.2f \n" % a)
def circulo (r):
    a = math.pi * math.pow(r, 2)
    print("\n El area del circulo es: %.2f \n" % a)

back = 1

while back == 1:
    print("Que area desea calcular? \n")
    print("1.- Triangulo")
    print("2.- Cuadrado")
    print("3.- Rectangulo")
    print("4.- Rombo")
    print("5.- Circulo")
    print("6.- Salir \n")
    n = int(input("Ingrese seleccion: "))

    if n == 1:
        print("-Area del triangulo")
        triangulo(float(input("Dame la medida de la base: ")), float(input("Dame la medida de la altura: ")))
    elif n == 2:
        print("-Area del cuadrado")
        cuadrado(float(input("Dame el medida del lado: ")))
    elif n== 3:
        print("-Area del rectangulo")
        rectangulo(float(input("Dame la medida de la base: ")), float(input("Dame la medida de la altura: ")))
    elif n == 4:
        print("-Area del rombo")
        rombo(float(input("Dame la medida de la diagonal mayor:  ")), float(input("Dame la medida de la diagonal menor: ")))
    elif n == 5:
        print("-Area del circulo")
        circulo(float(input("Dame el medida del radio: ")))
    elif n == 6:
        break
    else:
        print("\n **Nel, esa opcion no te la vengo manejando, ingresa una valida** \n")

    print("Presione una tecla para continuar...")
    msvcrt.getch()

    os.system("cls")
