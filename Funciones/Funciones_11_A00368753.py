import random

palabra = "anita"
letras = len(palabra)

def revuelvepalabra (palabra):

    c = 0
    while c < letras:
        desordenar = random.sample(palabra, letras)
        palabra = ''.join(desordenar)
        c = c + 1

    return palabra


print(revuelvepalabra(palabra))
