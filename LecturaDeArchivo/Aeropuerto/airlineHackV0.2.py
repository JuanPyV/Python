import math

origen = input("Origen: ")
destino = input("Destino: ")


def distancia_aeropuertos(origen, destino):
    try:
        aeropuerto = open("airports.txt", "r", encoding='UTF8')
        origenl = []
        destinol = []
        for linea in aeropuerto:
            lineaP = linea.strip()
            lin = lineaP.split(",")
            if lin[3].strip('"') == origen:
                origenl.append(lin)
            if lin[3].strip('"') == destino:
                destinol.append(lin)
        print(origenl)
        print(destinol)
        for airporto in range(len(origenl)):
            for airportd in range(len(destinol)):
                lat1 = origenl[airporto][6]
                lon1 = origenl[airporto][7]
                lat2 = destinol[airportd][6]
                lon2 = destinol[airportd][7]
                rad = math.pi / 180
                dlat = float(lat2) - float(lat1)
                dlon = float(lon2) - float(lon1)
                r = 6372.795477598
                a = math.pow(math.sin(rad*dlat/2), 2)+math.cos(rad*float(lat1))*math.cos(rad*float(lat2))*math.pow(math.sin(rad*dlon/2), 2)
                dist = 2 * r * math.asin(math.sqrt(a))
                print("De " + origenl[airporto][1] + " a " + destinol[airportd][1] + " hay: " + str(dist) + " km")

    except IOError:
            print("El archivo no existe")


distancia_aeropuertos(origen, destino)
