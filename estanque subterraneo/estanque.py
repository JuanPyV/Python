print("Este es un programa para calcular el perimetro, superficie aproximada y volumen de un estanque \n")

l = float(input("Ingresa el largo: "))
a = float(input("Ingresa la ancho: "))
pp = float(input("Ingresa la profundidad: "))

# Cree una nueva variable para reducir las operaciones de las otras
la = l*a

p = 2*(l+a)

v = la*pp

s = (p*pp)+la

print("El perimetro es: %.2f" % p)
print("El volumen es: %.2f" % v)
print("La superficie subterranea es: %.2f" % s)

# Autor: JuanPabloVelazco
