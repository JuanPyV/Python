
print("Programa para saber si el año es bisiesto")

x = int(input("Dame el año: "))
# Comprueba si es bisiesto
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print("El año %d es bisiesto" % x)
# Imprime que no es bisiesto si no cumple alguna de las 3 condiciones
else:
    print("El año %d no es bisiesto" % x)
# Autor: JuanPabloVelazco
