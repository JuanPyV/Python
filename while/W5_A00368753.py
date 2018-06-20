
n = int(input("¿Hasta que numero?  "))

c = 0
g = 0

while c < n:

    g = g + 3.785
    c = c + 1

    print("%d gal. equivale a %.3f lts" % (c, g))
