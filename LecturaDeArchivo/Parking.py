import numpy as np


a = np.random.randint(2, size=(10, 15))

np.savetxt("Lugares.txt", a, fmt="%d")

archivo = open("Lugares.txt", "r")

c = 0
for letter in archivo:
    lineaP = letter.strip()
    lin = lineaP.split(" ")
    print(lin)
    for n in lin:
        if n == "0":
            c = c + 1
print(c)



