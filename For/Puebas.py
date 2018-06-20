resp = "si"
suma = 0

while resp != "no":
    nom = input("Ingresa el nombre del alumno: ")
    ncal = int(input("Cuantas calificaciones: "))

    for i in range(1, ncal+1):
        cal = float(input("Ingresa la calificacion: "))
        suma = suma + cal

    prom = suma / ncal

    if prom >= 70:
        print("El alumno aprobo")
    else:
        print("El alumno reprobo")

    print("Desea ingresar otro alumno (si/no)")
    resp = input()


