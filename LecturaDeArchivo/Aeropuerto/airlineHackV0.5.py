aero = input("Nombre del aeropuerto: ")

def Aeropuertos_de_un_pais(aero):
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

Aeropuertos_de_un_pais(aero)
