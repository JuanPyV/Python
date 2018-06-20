# autor: JuanPabloVelazco

x = int(input("Cuantos empleados: "))
nx = 1
c = 1

while c <= x:

    n = float(input("Dame el sueldo:"))

    if n <= 1000:

        p = (n*.035) + 34.5 # Saco cuanto es la cantidad del porcentaje
        t = n-p

        print("Al empleado %d se le descuenta %.2f y su total es de %.2f" % (nx, p, t))

    elif n > 1000 and n <= 2500:

        p = (n * .12) + 67.30
        t = n - p

        print("Al empleado %d se le descuenta %.2f y su total es de %.2f" % (nx, p, t))

    else:

        p = (n * .23) + 211.20
        t = n - p

        print("Al empleado %d se le descuenta %.2f y su total es de %.2f" % (nx, p, t))

    nx = nx + 1 # contador para saber que numero de empleado es
    c = c + 1





