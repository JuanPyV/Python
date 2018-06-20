import math

d = float(input("Ingresa la distancia, en pies, desde la parte superior hasta la superficie del aceite: "))
r = float(input("Ingresa el radio del estanque en pies: "))

v1 = math.pi * (math.pow(r, 2)) * 200

v2 = math.pi * (math.pow(r, 2)) * d

vt = v1 - v2

print("El volumen de aceite es: %.2f" % vt)

