import math

back = "y"
while back == "y":
    print("Programa que calcule el area de un circulo, triangulo o cuadrado")
    print("1. Circulo")
    print("2. Cuadrado")
    print("3. Triangulo")

    opcion = input("Opcion: ")

    if opcion == "1":
        radio = float(input("El radio del circulo es: "))
        area = math.pi * radio ** 2
        print("El area del circulo de radio %.2f es %.2f" % (radio, area))
    elif opcion == "2":
        lado = float(input("La medida del lado es: "))
        area = lado * lado
        print("El area del cuadrado de lado %.2f es %.2f" % (lado, area))
    elif opcion == "3":
        base = float(input("La medida de la base es: "))
        altura = float(input("La medida de la altura es: "))
        area = (base*altura)/2
        print("El area del triangulo con base %.2f y altura %.2f es de %.2f" % (base, altura, area))
    else:
        print("Error, estas bien wey")
        back = str(input("Quieres continuar krnal: \n1.Yes\n2.No    "))