import math

ciudad = input("Ciudad: ")


def distancia_aeropuertos_de_ciudad(ciudad):
    try:
        aeropuerto = open("airports.txt", "r", encoding='UTF8')
        ciudadl = []
        for linea in aeropuerto:
            lineaP = linea.strip()
            lin = lineaP.split(",")
            if lin[3].strip('"') == ciudad:
                ciudadl.append(lin)
        print(ciudadl)
        for airport1 in range(len(ciudadl)):
            for airport2 in range(len(ciudadl)):
                lat1 = ciudadl[airport1][6]
                lon1 = ciudadl[airport1][7]
                lat2 = ciudadl[airport2][6]
                lon2 = ciudadl[airport2][7]
                if lat1 != lat2:
                    rad = math.pi / 180
                    dlat = float(lat2) - float(lat1)
                    dlon = float(lon2) - float(lon1)
                    r = 6372.795477598
                    a = math.pow(math.sin(rad*dlat/2), 2)+math.cos(rad*float(lat1))*math.cos(rad*float(lat2))*math.pow(math.sin(rad*dlon/2), 2)
                    dist = 2 * r * math.asin(math.sqrt(a))
                    print("De " + ciudadl[airport1][1] + " a " + ciudadl[airport2][1] + " hay: " + str(dist) + " km")

    except IOError:
            print("El archivo no existe")


distancia_aeropuertos_de_ciudad(ciudad)
