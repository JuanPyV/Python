# Escribir a palabra alreves
cadena = "hola "
for letra in (cadena[::-1]):
    print(letra)

palabra = "hola "
posicion = -1
for l in range(len(palabra)):
    print(palabra[posicion])
    posicion += -1


cadena1 = " adios "
for indice in range(len(cadena1)):
    print(cadena1[indice])


#Palindromo
p = "my gym"
p = p.replace(" ", "")
invertida = p[::-1]
if p == invertida:
    print(p, "es un palindrome")
else:
    print("no lo es")




# Cambiar letras en una palabra
cadena2 = "FabiolaUribe"
cambiada = ""

for letra2 in cadena2:
    if letra2 == "a":
        cambiada = cambiada + "4"
    elif letra2 == "i":
        cambiada = cambiada + "1"
    elif letra2 == "o":
        cambiada = cambiada + "0"
    elif letra2 == "e":
        cambiada = cambiada + "3"
    else:
        cambiada = cambiada + letra2
print(cambiada)


# Cambiar letra en una palabra
palabra2 = input("Dame la palabra")
lista = list(palabra2)
for pos in range(len(lista)):
    if lista[pos] in "Aa":
        lista[pos] = ("4")
    elif lista[pos] in "Ee":
        lista[pos] = ("3")
palabra2 = "".join(lista)
print(palabra2)


#Saber el num max, promedio y suma
num = [58, 3, 72, 1, 56]
s = 0
max = num[0]
for n in num:
    s += n
    if n > max:
        max = n

pro = s / len(num)

print("La suma es: %d" % s)
print("El promedio es: %d" % pro)
print("El mayor es: %d" % max)




