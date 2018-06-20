import math

print("Programa para calcular area lateral y volumen de cilindro\n")

r = float(input("Ingresa el radio: "))

h = float(input("Ingresa la altura: "))

al = 2*math.pi*r*h

# Esto saca el area de la base teniendo el radio
ab = math.pi*(math.pow(r, 2))

v = ab*h

print("El area lateral es: {0:.2f}, y el volumen es: {1:.2f}".format(al, v))

# Autor: JuanPabloVelazco
