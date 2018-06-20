n = int(input("Dame hasta que numero: "))
c = 0
for x in range (1, (n+1)):
    if x%2 == 0:
        c = c-x
    else:
        c = c+x
print("El resultado es: %d" % c)

