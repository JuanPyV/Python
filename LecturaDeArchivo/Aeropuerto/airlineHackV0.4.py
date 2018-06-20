airport_codex=input("From(airport code): ")
cityx=input("To(city): ")
countryx=input("(country): ")


def airports_codez (airport_code, city, country):
    try:
        with open('airports.txt', 'r', encoding='UTF8') as airports_file:
            airports_code_list=[]
            for line in airports_file:
                lines=line.strip()
                airport_list=lines.split(",")
                if airport_list[3].strip('"')==country:
                    if airport_list[2].strip('"')==city:
                        airports_code_list.append(airport_list[4].strip('"'))
        with open('routes.txt','r', encoding='UTF8') as routes_file:
            airports_routes_list=[]
            for line_r in routes_file:
                lines_r=line_r.strip()
                routes_list=lines_r.split(",")
                if routes_list[2].strip('"')==airport_code:
                    for element in range(len(airports_code_list)):
                        if routes_list[4].strip('"')==airports_code_list[element]:
                            airports_routes_list.append(routes_list[0].strip('"'))
        with open('airlines.txt', 'r', encoding='UTF8') as airlines_file:
            airlines_names_list=[]
            airline_alias=[]
            for line_a in airlines_file:
                lines_a=line_a.strip()
                airlines_list=lines_a.split(",")
                for element in range(len(airports_routes_list)):
                    if airlines_list[3].strip('"')==airports_routes_list[element]:
                        airlines_names_list.append(airlines_list[1].strip('"'))
                        airline_alias.append(airlines_list[2].strip('"'))
        for code in range(len(airports_routes_list)):
            print("La aerolinea " + airlines_names_list[code] + " con codigo: " + airports_routes_list[code])



    except IOError:
        print("Error: File Not Found")

airports_codez(airport_codex, cityx, countryx)