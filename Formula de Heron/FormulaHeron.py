import math

print("Programa para calcular el area de un triangulo con la formula de Heron \n")

a = float(input("Ingresa el lado a: "))
b = float(input("Ingresa el lado b: "))
c = float(input("Ingresa el lado c: "))

s = (a+b+c)/2

ar = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("\nEl area es: %.1f" % ar)
