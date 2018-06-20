from math import sin, cos, sqrt, atan2
def latitud(ciudad):
    try:
        archivo=open("airports.txt","r",encoding="UTF-8")
    except:
        print("No se puede abrir el archivo")
    else:
        lista2=[]
        for linea in archivo:
            lista=linea.split(",")
            lista[2]=lista[2].strip(' " ')
            if lista[2] == ciudad:
                return lista[6]

def longitud(ciudad):
    try:
        archivo=open("airports.txt","r",encoding="UTF-8")
    except:
        print("No se puede abrir el archivo")
    else:
        lista2=[]
        for linea in archivo:
            lista=linea.split(",")
            lista[2]=lista[2].strip(' " ')
            if lista[2] == ciudad:
                return lista[7]
def Haversine(lat1,long1,lat2,long2):
    dlat=lat2-lat1
    dlong=long2-long1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * (sin(dlong/2)**2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = 6378 * c
    return distance
def aeropuertos(pais):
    try:
        archivo=open("airports.txt","r",encoding="UTF-8")
    except:
        print("No se puede abrir el archivo")
    else:
        aeropuertos=[]
        for linea in archivo:
            lista=linea.split(",")
            lista[3]=lista[3].strip(' " ')
            if lista[3] == pais:
                resultado=[lista[1],lista[6],lista[7]]
                aeropuertos.append(resultado)
    return aeropuertos

def distancias():
    arch_distancias=open("Distancias.txt",'w+')
    airports=aeropuertos(pais)
    for airport1 in range(len(airports)):
        for airport2 in range(len(airports)):
            lat1=float(airports[airport1][1])
            long1=float(airports[airport1][2])
            lat2=float(airports[airport2][1])
            long2=float(airports[airport2][2])
            print("La distancia de")
            print(Haversine(lat1,long1,lat2,long2))

pais="North Korea"
distancias()