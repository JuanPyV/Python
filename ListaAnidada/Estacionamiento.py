park = [[1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]]


def estacionamiento(listaP):
    row = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    freeparking = []
    freeslot = 0

    for letter in range(len(listaP)):
        for slot in range(len(listaP[letter])):
            if listaP[letter][slot] == 0:
                d = str(slot + 1)
                listaP[letter][slot] = row[letter] + d
                freeparking.append(listaP[letter][slot])
                freeslot = freeslot + 1
    print("\n Hay", freeslot, "lugares vacio ")
    return ", ".join(freeparking)


print("\n           ESTACIONAMIENTO VARGAS\n")

print("Los lugares vacios estan en: ", estacionamiento(park))
