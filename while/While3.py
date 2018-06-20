
n = int(input("cuantas veces: "))

resultado = 0
contador = 1

while contador <= n:

    if contador % 2 == 0:

        resultado = resultado - contador
        contador = contador + 1

    else:

        resultado = contador + resultado
        contador = contador + 1

print(resultado)


