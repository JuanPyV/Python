import math

print("\n Programa para imprimir la hipotenusa y los angulos agudos a partir de sus catetos \n")

print("        |\                     ")
print("        |  \                   ")
print("        |    \                 ")
print("        |      \               ")
print("     b  |        \   c         ")
print("        |          \           ")
print("        |            \         ")
print("        |______________\       ")
print("              a              \n")

a = float(input("Ingresa el cateto a: "))
b = float(input("Ingresa el cateto b: "))

c = math.sqrt((a*a+b*b))

aa = math.acos(a/c)

# Esto es para convertir de radianes a grados
aag = math.degrees(aa)

ab = 90-aag

print("La hipotenusa es: " + str(c) + " el angulo C es: " + str(aag) + " y el angulo B es: " + str(ab))

# Autor: JuanPabloVelazco
