import math

a = float(input("Dame el valor de a: "))

# Saca el area del rectangulo
b = 2*a
r = a/2
# Saca el area del parte sombreada
A = (a*b)-((math.pi*math.pow(r, 2)) * 2)

print("El area sombreada es: %.2f" % A)

# Autor: JuanPabloVelazco A00368753