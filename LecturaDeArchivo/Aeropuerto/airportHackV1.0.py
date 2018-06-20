# Autores: Juan Pablo Velazco Velasquez y Luis Gerardo Delgado

import math
import os
import msvcrt
import time


# 1°
def aeropuertos_de_un_pais(country):
    try:
        aeropuerto = open("airports.txt", "r", encoding='UTF8')
        lineas = []
        for linea in aeropuerto:
            lineaP = linea.strip()
            lin = lineaP.split(",")
            if lin[3].strip('"') == country:
                lineas.append(lin)
        for airport in lineas:
            print("Aeropuerto:" + airport[1].strip('"') + " Pais: " + airport[2].strip('"') + " Codigo:" + airport[
                4].strip('"'))

    except IOError:
        print("El archivo no existe")


# 2°
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
                a = math.pow(math.sin(rad * dlat / 2), 2) + math.cos(rad * float(lat1)) * math.cos(
                    rad * float(lat2)) * math.pow(math.sin(rad * dlon / 2), 2)
                dist = 2 * r * math.asin(math.sqrt(a))
                print("De " + origenl[airporto][1] + " a " + destinol[airportd][1] + " hay: " + str(dist) + " km")

    except IOError:
        print("El archivo no existe")


# 3°
def distancia_aeropuertos_de_pais(pais):
    try:
        aeropuerto = open("airports.txt", "r", encoding='UTF8')
        paisl = []
        for linea in aeropuerto:
            lineaP = linea.strip()
            lin = lineaP.split(",")
            if lin[3].strip('"') == pais:
                paisl.append(lin)
        now = time.strftime("%d-%m-%y")
        distancia = open("Distancias_Entre_Aeropuertos " + now + ".txt", "w+", encoding='UTF8')
        for airport1 in range(len(paisl)):
            for airport2 in range(len(paisl)):
                lat1 = paisl[airport1][6]
                lon1 = paisl[airport1][7]
                lat2 = paisl[airport2][6]
                lon2 = paisl[airport2][7]
                if lat1 != lat2:
                    rad = math.pi / 180
                    dlat = float(lat2) - float(lat1)
                    dlon = float(lon2) - float(lon1)
                    r = 6372.795477598
                    a = math.pow(math.sin(rad * dlat / 2), 2) + math.cos(rad * float(lat1)) * math.cos(
                        rad * float(lat2)) * math.pow(math.sin(rad * dlon / 2), 2)
                    dist = 2 * r * math.asin(math.sqrt(a))
                    distancia.write("De " + paisl[airport1][1] + " a " + paisl[airport2][1] + " hay: " + str(dist) + " km \n")
                    print("De " + paisl[airport1][1] + " a " + paisl[airport2][1] + " hay: " + str(dist) + " km")

    except IOError:
        print("El archivo no existe")


# 4°
def airports_codez(airport_code, city, country):
    try:
        with open('airports.txt', 'r', encoding='UTF8') as airports_file:
            airports_code_list = []
            for line in airports_file:
                lines = line.strip()
                airport_list = lines.split(",")
                if airport_list[3].strip('"') == country:
                    if airport_list[2].strip('"') == city:
                        airports_code_list.append(airport_list[4].strip('"'))
        with open('routes.txt', 'r', encoding='UTF8') as routes_file:
            airports_routes_list = []
            for line_r in routes_file:
                lines_r = line_r.strip()
                routes_list = lines_r.split(",")
                if routes_list[2].strip('"') == airport_code:
                    for element in range(len(airports_code_list)):
                        if routes_list[4].strip('"') == airports_code_list[element]:
                            airports_routes_list.append(routes_list[0].strip('"'))
        with open('airlines.txt', 'r', encoding='UTF8') as airlines_file:
            airlines_names_list = []
            airline_alias = []
            for line_a in airlines_file:
                lines_a = line_a.strip()
                airlines_list = lines_a.split(",")
                for element in range(len(airports_routes_list)):
                    if airlines_list[3].strip('"') == airports_routes_list[element]:
                        airlines_names_list.append(airlines_list[1].strip('"'))
                        airline_alias.append(airlines_list[2].strip('"'))
        for code in range(len(airports_routes_list)):
            print("La aerolinea " + airlines_names_list[code] + " con codigo: " + airports_routes_list[code])

    except IOError:
        print("Error: File Not Found")


# 5°
def aerolineas_aeropuerto(aero):
    try:
        aeropuerto = open("airports.txt", "r", encoding='UTF8')
        lineas = []
        for linea in aeropuerto:
            lineaP = linea.strip()
            lin = lineaP.split(",")
            if lin[1].strip('"') == aero:
                lineas.append(lin)
        for elem in range(len(lineas)):
            code = lineas[elem][4]
        rutas = open("routes.txt", "r", encoding='UTF8')
        lineasR = []
        for linea in rutas:
            lineaR = linea.strip()
            linR = lineaR.split(",")
            if linR[2].strip('"') or linR[4].strip('"') == code:
                lineasR.append(linR)
        for elemR in range(len(lineasR)):
            codeR = lineasR[elem][0]
        aerolineas = open("airlines.txt", "r", encoding='UTF8')
        lineasA = []
        aerolineas_lista = []
        for linea in aerolineas:
            lineaA = linea.strip()
            linA = lineaA.split(",")
            lineasA.append(linA)
        for elemA in range(len(lineasA)):
            if codeR == lineasA[elemA][3].strip('"'):
                aerolineas_lista.append(lineasA[elemA][1])
        for elemAir in aerolineas_lista:
            print("La aerolinea " + elemAir + " tiene actividad en el aeropuerto indicado")

    except IOError:
        print("El archivo no existe")


# 6°
def destinations_X(airline, airport):
    try:
        with open('airlines.txt', 'r', encoding='UTF8') as airlines_file:
            aCodes_list = []
            for lineA in airlines_file:
                linesA = lineA.strip()
                airlines_list = linesA.split(",")
                if airlines_list[1].strip('"') == airline:
                    aCodes_list.append(airlines_list[3].strip('"'))
        with open('airports.txt', 'r', encoding='UTF8') as airports_file:
            airCodes_list = []
            fromCountryList = []
            fromCityList = []
            for lineAr in airports_file:
                linesAr = lineAr.strip()
                airports_list = linesAr.split(",")
                if airports_list[1].strip('"') == airport:
                    airCodes_list.append(airports_list[4].strip('"'))
                    fromCountryList.append(airports_list[3].strip('"'))
                    fromCityList.append(airports_list[2].strip('"'))
                    lat0 = airports_list[6]
                    lon0 = airports_list[7]
        with open('routes.txt', 'r', encoding='UTF8') as routes_file:
            destinations_list = []
            for line in routes_file:
                lines = line.strip()
                routes_list = lines.split(",")
                for element in range(len(aCodes_list)):
                    for elementx in range(len(airCodes_list)):
                        if routes_list[0].strip('"') == aCodes_list[element] and routes_list[2].strip('"') == \
                                airCodes_list[elementx]:
                            destinations_list.append(routes_list[4].strip('"'))
        with open('airports.txt', 'r', encoding='UTF8') as aNames_file:
            aNames_list = []
            toCountryList = []
            toCityList = []
            lats = []
            lons = []
            for lineArn in aNames_file:
                linesArn = lineArn.strip()
                airportsN_list = linesArn.split(",")
                for elementz in range(len(destinations_list)):
                    if airportsN_list[4].strip('"') == destinations_list[elementz]:
                        toCountryList.append(airportsN_list[3].strip('"'))
                        toCityList.append(airportsN_list[2].strip('"'))
                        lats.append(airportsN_list[6].strip('"'))
                        lons.append(airportsN_list[7].strip('"'))
                        aNames_list.append(airportsN_list[1].strip('"'))
            lat1 = lats[0]
            lon1 = lons[0]
            lat2 = lats[1]
            lon2 = lons[1]
            airportsDistanceFile = open("Distances.txt", "w+")
            for elementp in range(len(lons)):
                distances = []
                rad = math.pi / 180
                dlat = float(lats[elementp]) - float(lat0)
                dlon = float(lons[elementp]) - float(lon0)
                r = 6372.795477598
                a = math.pow(math.sin(rad * dlat / 2), 2) + math.cos(rad * float(lat0)) * math.cos(
                    rad * float(lats[elementp])) * math.pow(math.sin(rad * dlon / 2), 2)
                dist = 2 * r * math.asin(math.sqrt(a))
                airportsDistanceFile.write(
                    " De " + fromCityList[0] + " a " + aNames_list[elementp] + " hay: " + str(dist) + " km. \n")
                distances.append(dist)
            print("Longest distance is from: " + aNames_list[elementp] + ". With a distance of: " + str(
                max(distances)) + "km \n")

    except IOError:
        print("Error: File Not Found")


back = 1

while back == 1:
    print("Aeropuertos")
    print("Que accion desea realizar? \n")
    print("1.- Aeropuertos de un pais")
    print("2.- Distancia entre aeropuertos")
    print("3.- Distancia entre aeropuertos de un pais")
    print("4.- Aerolineas que van a un destino desde un determinado aeropuerto")
    print("5.- Aerolineas que operan en un determinado aeropuerto")
    print("6.- Destinos de una aerolinea desde un determinado aeropuerto")
    print("7.- Salir \n")
    n = int(input("Ingrese seleccion: "))

    if n == 1:
        print("-Aeropuertos de un pais")
        aeropuertos_de_un_pais(input("Dame el pais: "))
    elif n == 2:
        print("-Distancia entre aeropuertos")
        distancia_aeropuertos(input("Dame el origen: "), input("Dame el destino: "))
    elif n == 3:
        print("-Distancia entre aeropuertos de un pais")
        distancia_aeropuertos_de_pais(input("Dame el pais: "))
    elif n == 4:
        print("-Aerolineas que van a un destino desde un determinado aeropuerto")
        airports_codez(input("Dame codigo de aeropuerto:  "), input("Dame la ciudad: "), input("Dame el pais: "))
    elif n == 5:
        print("-Aerolineas que operan en un determinado aeropuerto")
        aerolineas_aeropuerto(input("Dame el nombre del aeropuerto: "))
    elif n == 6:
        print("-Destinos de una aerolinea desde un determinado aeropuerto")
        destinations_X(input("Dame la aerolinea: "), input("Dame el aeropuerto: "))
    elif n == 7:
        break
    else:
        print("\n **Opcion incorrecta, por favor seleccione una opcion valida** \n")

    print("Presione una tecla para continuar...")
    msvcrt.getch()

    os.system("cls")
