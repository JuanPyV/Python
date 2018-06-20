# Autor: Juan Pablo Velazco A00368753

import math
import os
import msvcrt

def grados (c):
    f = (c * 9/5) + 32
    print("\n %.2f° Celsius equivalen a: %.2f° Farenheit \n" % (c, f))
def triangulo (a, b):
    c = math.sqrt((a * a + b * b))
    aa = math.acos(a / c)
    aag = math.degrees(aa)
    ab = 90 - aag
    print("\n La hipotenusa es: %.2f el angulo C es: %.2f y el angulo B es: %.2f" % (c, aag, ab))
def conversor (ft):
    cm = ft * 30.48
    m = ft * .304
    inch = ft * 12
    yrd = ft * .333
    print(" \n %.2f pies es equivalente a %.2f centimetros" % (ft, cm))
    print(" \n %.2f pies es equivalente a %.2f metros" % (ft, m))
    print(" \n %.2f pies es equivalente a %.2f pulgadas" % (ft, inch))
    print(" \n %.2f pies es equivalente a %.2f yardas" % (ft, yrd))
def cilindro (r, h):
    al = 2 * math.pi * r * h
    ab = math.pi * (math.pow(r, 2))
    v = ab * h
    print("\n El area lateral es: %.2f, y el volumen es: %.2f" % (al, v))
def heron (a, b, c):
    s = (a + b + c) / 2
    ar = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("\n El area es: %.1f" % ar)

back = 1

while back == 1:
    print("Que programa desea usar? \n")
    print("1.- Convertir grados Celsius a Farenheit")
    print("2.- Calcular hipotenusa y angulos agudos")
    print("3.- Conversor de unidades")
    print("4.- Area lateral y volumen de cilindro")
    print("5.- Area de un triangulo con formula de Heron")
    print("6.- Salir \n")
    n = int(input("Ingrese seleccion: "))

    if n == 1:
        print("-Convertir grados Celsius a Farenheit")
        grados(float(input("Dame los grados en Celsius: ")))
    elif n == 2:
        print("-Calcular hipotenusa y angulos agudos")
        print("                               ")
        print("        |\                     ")
        print("        |  \                   ")
        print("        |    \                 ")
        print("        |      \               ")
        print("     b  |        \   c         ")
        print("        |          \           ")
        print("        |            \         ")
        print("        |______________\       ")
        print("              a              \n")
        triangulo(float(input("Ingresa el cateto a: ")), float(input("Ingresa el cateto b: ")))
    elif n == 3:
        print("-Conversor de unidades")
        conversor(float(input("Ingresa la medida en pies: ")))
    elif n == 4:
        print("-Area lateral y volumen de cilindro")
        cilindro(float(input("Ingresa el radio: ")), float(input("Ingresa la altura: ")))
    elif n == 5:
        print("-Area de un triangulo con formula de Heron")
        heron(float(input("Ingresa el lado a: ")), float(input("Ingresa el lado b: ")), float(input("Ingresa el lado c: ")))
    elif n == 6:
        print("\n Hasta luego!! ")
        msvcrt.getch()
        break
    else:
        print("\n **Nel, esa opcion no te la vengo manejando, ingresa una valida** \n")

    print("Presione una tecla para continuar...")
    msvcrt.getch()

    os.system("cls")

    

