import math

r = float(input("Dame el radio menor: "))
R = float(input("Dame el radio mayor: "))
h = float(input("dame la altura: "))

# Si el valor de R es + comprueba el de r y si tambien lo es comprueba h
if R > 0:
    if r > 0:
        if h > 0:
            # Formula para sacar el volumen
            v = ((1/3)*math.pi*h)*(pow(R, 2)+pow(r, 2)+(R*r))

            print("El volumen es: %.2f" % v)

        else:
            print("Dato de altura incorrecto, verifica")
    else:
        print("Dato de radio menor incorrecto, verifica")
else:
    print("Dato de radio mayor incorrecto, verifica")

# Autor: JuanPabloVelazco
