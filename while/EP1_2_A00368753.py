# autor: JuanPabloVelazco

x = int(input("Hasta que numero: "))
c = 1
i = 2

print(i)

while c < x: # Compruebo que el contador sea menor al valor ingresado

    if i % 2 == 0:  # Comprueba si es par
        i = i + 5
        print(i)

    else:
        i = i - 3
        print(i)

    c = c + 1
