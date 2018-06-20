import math
airlinex=input("Airline: ")
airportx=input("From(airport): ")
def destinations_X (airline, airport):
    try:
        with open('airlines.txt', 'r', encoding='UTF8') as airlines_file:
            aCodes_list=[]
            for lineA in airlines_file:
                linesA=lineA.strip()
                airlines_list=linesA.split(",")
                if airlines_list[1].strip('"')==airline:
                    aCodes_list.append(airlines_list[3].strip('"'))
        with open('airports.txt', 'r', encoding='UTF8') as airports_file:
            airCodes_list=[]
            fromCountryList=[]
            fromCityList=[]
            for lineAr in airports_file:
                linesAr=lineAr.strip()
                airports_list=linesAr.split(",")
                if airports_list[1].strip('"')==airport:
                        airCodes_list.append(airports_list[4].strip('"'))
                        fromCountryList.append(airports_list[3].strip('"'))
                        fromCityList.append(airports_list[2].strip('"'))
                        lat0=airports_list[6]
                        lon0=airports_list[7]
        with open('routes.txt', 'r', encoding='UTF8') as routes_file:
            destinations_list=[]
            for line in routes_file:
                lines=line.strip()
                routes_list=lines.split(",")
                for element in range(len(aCodes_list)):
                    for elementx in range(len(airCodes_list)):
                        if routes_list[0].strip('"')==aCodes_list[element] and routes_list[2].strip('"')==airCodes_list[elementx]:
                            destinations_list.append(routes_list[4].strip('"'))
        with open('airports.txt', 'r', encoding='UTF8') as aNames_file:
            aNames_list=[]
            toCountryList=[]
            toCityList=[]
            lats=[]
            lons=[]
            for lineArn in aNames_file:
                linesArn=lineArn.strip()
                airportsN_list=linesArn.split(",")
                for elementz in range(len(destinations_list)):
                    if airportsN_list[4].strip('"')==destinations_list[elementz]:
                        toCountryList.append(airportsN_list[3].strip('"'))
                        toCityList.append(airportsN_list[2].strip('"'))
                        lats.append(airportsN_list[6].strip('"'))
                        lons.append(airportsN_list[7].strip('"'))
                        aNames_list.append(airportsN_list[1].strip('"'))
            lat1=lats[0]
            lon1=lons[0]
            lat2=lats[1]
            lon2=lons[1]
            airportsDistanceFile=open("Distances.txt","w+")
            for elementp in range(len(lons)):
                distances=[]
                rad = math.pi / 180
                dlat = float(lats[elementp]) - float(lat0)
                dlon = float(lons[elementp]) - float(lon0)
                r = 6372.795477598
                a = math.pow(math.sin(rad*dlat/2), 2)+math.cos(rad*float(lat0))*math.cos(rad*float(lats[elementp]))*math.pow(math.sin(rad*dlon/2), 2)
                dist = 2 * r * math.asin(math.sqrt(a))
                airportsDistanceFile.write(" De " + fromCityList[0] + " a " + aNames_list[elementp] + " hay: " + str(dist) + " km. \n")
                distances.append(dist)
            print("Longest distance is from: " + aNames_list[elementp] + ". With a distance of: " + str(max(distances)) + "km \n")

    except IOError:
        print("Error: File Not Found")

destinations_X(airlinex, airportx)