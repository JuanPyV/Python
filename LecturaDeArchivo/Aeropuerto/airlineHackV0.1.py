country = input("Country: ")


def Aeropuertos_de_un_pais(country):
    try:
        aeropuerto = open("airports.txt", "r", encoding='UTF8')
        lineas = []
        for linea in aeropuerto:
            lineaP = linea.strip()
            lin = lineaP.split(",")
            if lin[3].strip('"') == country:
                lineas.append(lin)
        for airport in lineas:
            print("Airport:" + airport[1].strip('"') + " City: " + airport[2].strip('"') + " Code:" + airport[4].strip('"'))

    except IOError:
            print("El archivo no existe")

Aeropuertos_de_un_pais(country)
