p = input("Ingresa una palabra: ")
v = input("Ingresa otra palabra: ")


def coincidencias (p):
    c = 0
    i = 0
    for n in p:
        if n in v[i]:
            c = c+1
            i = i+1
    return c


print(coincidencias(p))
