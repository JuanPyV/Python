
listaA = [[1, 5, 8, 9, -11], [-1, 8, 9], [5, 4, 8, 10]]
c = 0
s = 0
p = 0
n = 0

# Dice cuantos valores de la listas son pares
for lista in listaA:
    for elem in lista:
        if elem % 2 == 0:
            c = c + 1
print(c)

# Suma todos los valores de las listas
for suma in listaA:
    for elem2 in suma:
        s = elem2 + s
print(s)

#cuantos numeros son positivos
for positivo in listaA:
    for elem3 in positivo:
        if elem3 >= 0:
            p = p + 1
print(p)

#Cambiar negativo por 0
for neg in range(len(listaA)):
    for elem4 in listaA[neg]:
        if elem4 <= 0:
            listaA[neg][elem4] = 0
    print(listaA)








n = 0
m = 4
listaA[n][m] = 0
print(listaA)




