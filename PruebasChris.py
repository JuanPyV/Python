# A01540405
# Examen final

""" Se importan las siguientes librerias para poder trabajar con el archivo y desarrolar el programa """

import os
import csv

""" Se exporta el archivo, se especifica que solo se desea exportarlo para poder leerlo """

f = open('listaActividades.csv', 'r')
archivo = csv.reader(f)
""" Se agrega una lista vacia en la cual se van a recibir los datos del archivo exportado,se crea una lista de listas"""
lista = []
listaPromedio = []

for row in archivo:
    lista = lista + [row]

""" Revisa el numero de elementos en la lista """
tam = len(lista)

""" 
Se realiza una función para poder sacar el promedio general de calificaciones del grupo 

El rango queda especificado de tal manera que solo nos interesa conocer las calificaciones de los alumnos por lineas, 
no necesitamos la primera linea que se muestra lo que tenemos por columanas en el documento

Se debe utilizar 'float' debido a que en la lista de calificaciones no todos son enteros

Cabe destacar que todo el docuemto de excel se encuentra guuardado como escritura aunque no presisamente sean palabras

'c' se encuentra igualado a '-1' para que pueda empezar a contar desde 0 y los resultados sean los correctos

Despues de hacer la suma en de toda la lista y hacer el cambio de 'x' por 'num' se debe de dividir entre '5' que es el 
el total de todas las calificaciones y ese resultado se debera dividir entre '15' que es el total de los alumnos, todo 
esto dentro de una nueva variable, para poder llamarla a imprimir. Dentro de la impresion la colocacion del'%.2f' le 
esta pidiendo al programa que imprima despues del valor entero 2 puntos decimales los cuales se encuentran en float. 

"""


def promedioGrupo(lista):
    num = 0
    y = 0
    for n in range(1, 15):
        c = -1
        for i in range(len(lista[n])):
            c += 1
            if c != 0:
                x = float(lista[n][c])
                num += x
                y = (num / 5) / 15

    print("\nEL promedio grupal es de %.2f" % y + "\n")


""" 

Se realiza una función para poder sacar el promedio final por cada alumno

'pop' borra el numero de la lista que indiques en este caso borra la primera linea en donde se encuentran las act. y nom

Esta variable hace casi lo mismo que la anterior solo que una de las diferencias es que esta variable cuenta con un 
conrador para poder deliminar las lineas para que solo sume las actividades de alumno por alumno de igual manera se
utiloza el 'float' y 'append' el cual me agrega lo indicado a lo ultimo de mi lista sin mover lo anterior. Otra de las
diferencias es que esta solo me divide mi promedio entre '5' que es el numero de mis actividades 

Considere mas facil que dentro de esta misma funcion se pudiera obtener el mejor y el peor alumno de todo el grupo, ya 
que se obtenia el promedio individual así que solo mandaba llamar ek 'max' (mejor alumno)  y el 'min' (peor alumno) de
mi lista, una vez determinada la mandaba llamar junto con archivo para conocer el nombre del alumno el cual indica que
se va a encontrar en la posicion '0'

"""


def calAlumno(archivo):
    lista = []
    listaCal = []
    for row in archivo:
        lista.append(row)
    lista.pop(0)

    for n in range(len(lista)):
        c = 0
        num = 0
        y = 0

        for i in range(len(lista[n])):
            c += 1

            if i != 0:
                if c <= 6:
                    x = float(lista[n][i])
                    num += x
                    y = num / 5
        listaCal.append(y)
        print("El promedio de " + lista[n][0] + " es de %.2f" % y)
        mejorAlumno = listaCal.index(max(listaCal)) + 1
        peorAlumno = listaCal.index(min(listaCal)) + 1
    print("\nEl alumno mas mejor es " + archivo[mejorAlumno][0])
    print("El alumno mas peor es " + archivo[peorAlumno][0])


"""

Utilice como inicio de funcion la que usted nos proporciono en el documento solo que cambie algunas variables para mi 
entendimiento en el programa. La funcion obtiene la suma de cada una de las actividades (por columnas) y poder encontrar
la actividad mas dificil y la actividad mas facil, esto dependia del valor mas alto (mas facil) y el valor mas bajo (mas 
dificil), el rango indica que el conteo empiece en uno que es en donde se encuentra la primera actividad hasta la ultima 
actividad. Su funcionalidad es sumar el promedio de la actividad.

"""


def sumColMatrix(n, lista, col):
    s = 0
    for i in list(range(1, n)):
        s = s + float(lista[i][col])
    return s


""" 

Se define una funcion algo parecida al promedio general ya que su objetivo es que corra toda la lista de datos de 
calificaciones para que cuando el valor sea igual '0' de detenga y guarde este dato dentro de la lista vacia el cual una 
vez de que la lista deje de estar vacia y guarde el numero de la columna en la que se encuentra agregar un 'append' para 
que dentro de esta lista se agrege la posicion '0' que me dara a conocer el nombre de este alumno y ya despues se mandara 
llamar para imprimir al alumno que tenga esta calificacion 

"""


def noTarea(lista):
    alumSinTarea = []
    for O in lista:
        for C in range(len(O)):
            if C != 0:
                if O[C] == "0":
                    alumSinTarea.append(O[0])
    print("El alumno que no hizo la tarea es: ", alumSinTarea[0])


""" 

Se realiza una función que reciba una lista (la cual es la del archivo), se general dos listas vacias para la obtencion 
de datos. Mi lista se va a recorrer de 'rango(1,6)'por que no quiero la primera fila (que es donde se encuentran los 
nombres de los alumnos).

Se guardan los nuevos promedios de los alumnos en una lista, con un 'for' se recorre esa misma lista con los promedios y 
con un 'if' se encuentra quien tiene el promedio mayor o igual a 80 dejando a los que no tengan ese promedio como una 
lista vacia, despues se genera una nueva lista donde obtiene los indices buscas el índice de la actividad 5. Despues 
dentro de esta misma funcion se vuelve a crear otro if para encontrar quien tiene mayor calificación de 90 en esa 
actividad, y guardas dentro de la lista con la posicion '[0] para obtener tambien el nombre de la persona, ya por ultimo 
se agrega un elif para ver si la calificación es menor o igual a 70 (este valor por lo mencionado) los datos obtenidos 
se guardan en la otra lista ' listaPromedioMenor' para despues mandarla llamar e imprimir los resultados, de quien 
mereceria  los puntos extras y quienes son los alumnos reprobados

PD: Maestra, si decidi cambiar el valor  de 60 por 70 para que mi lista no quedara vacia, segun vi el calor que se que 
se indicara no cambiaba mucho la programacion, la unica diferencia es que no se guardaba nada y apodia aparecer como 
error o solo inicaba que no habia nungun dato en la lista e imprimia que no habia reprobados esto segun como se 
estructurara la funcion, el motivo de cambiarlo por 70 para obtener un resultado dentro de la lista e imprimirlo y a mi 
parecer tambien por estica dentro del docuemto  y también porque dentro del Tec el 70 es la calificacion aprovatoria :D

 """


def puntoExtra(lista):
    listaPromedioMayor = []
    listaPromedioMenor = []
    for i in lista:
        suma = 0
        for e in range(1, 6):
            suma = suma + float(i[e])
        promedio = suma / 5
        if promedio >= 80 and i[5] >= "90":
            listaPromedioMayor.append(i[0])
        elif promedio <= 70:
            listaPromedioMenor.append(i[0])

    print("Merecen participacion: " + listaPromedioMayor[0] + " y " + listaPromedioMayor[1])
    print("Reprobaron estos alumnos: " + listaPromedioMenor[0] + " , " + listaPromedioMenor[1] + " y " +
          listaPromedioMenor[2])


""" 
Se define una funcion en donde se va a recibir una lista 

"""


def caliFinal(lista):
    listaCali = []
    for i in lista:
        tresActs = 0
        cuartaAct = 0
        quintaAct = 0
        caliFinal = 0
        for e in range(1, 4):
            tresActs = tresActs + float(i[e])
        promedioTresActividades = (tresActs / 3) * .5
        for f in range(4, 5):
            cuartaAct = (cuartaAct + float(i[f])) * .2
        for d in range(5, 6):
            quintaAct = (quintaAct + float(i[d])) * .3
        caliFinal = promedioTresActividades + quintaAct + cuartaAct
        listaCali.append(caliFinal)
        print("El promedio final de", i[0], "es de: %.2f" % caliFinal)
    for n in range(len(listaCali)):
        if listaCali[n] == max(listaCali):
            print("\n" + lista[n][0] + " tiene el mejor promedio de todos %.2f" % max(listaCali))
    for n in range(len(listaCali)):
        if listaCali[n] == min(listaCali):
            print(lista[n][0] + " tiene el pior promedio de todos %.2f" % min(listaCali))


def alumnoMas(lis):
    lista = []
    for i in lis:
        suma = 0
        for n in range(1, 6):
            suma = suma + float(i[n])
        promedio = suma / 5
        lista.append(promedio)
        y = lista.index(max(lista))
    print("El mejor alumno es: ", lis[y][0])


def alumnoMenos(lis):
    lista = []
    for i in lis:
        suma = 0
        for e in range(1, 6):
            suma = suma + float(i[e])
        promedio = suma / 5
        lista.append(promedio)
        y = lista.index(min(lista))
    print("El peor alumno es: ", lis[y][0])


for num in range(1, 6):
    acum = sumColMatrix(tam, lista, num)
    promedio = acum / (tam - 1)
    listaPromedio.append(promedio)

""" Se indican cuales funciones de arriba tienen que imprimirse y se agrega el orden de ellas mismas  """

lista2 = lista
lista2.pop(0)
tam = len(lista2)

calAlumno(lista)
promedioGrupo(lista)
alumnoMas(lista2)
alumnoMenos(lista2)
noTarea(lista2)
puntoExtra(lista2)
x = listaPromedio.index(min(listaPromedio)) + 1
print("La actividad mas dificil es: " + str(x))
y = listaPromedio.index(max(listaPromedio)) + 1
print("La actividad mas facil es: " + str(y))
print("\n---- Calificaciones Finales ----")
print(caliFinal(lista2))

""" Finalizacion final del programa (lo cierra) """

f.close()