x1 = float(input("Ingresa X1\n"))
x2 = float(input("Ingresa X2\n"))
y1 = float(input("Ingresa Y1\n"))
y2 = float(input("Ingresa Y2\n"))

dist = (((x2-x1)**2)+((y2-y1)**2))**.5

print("El valor de la distancia entre los puntos %f, %f y %f, %f es de: %f " % (x1, y1, x2, y2, dist))



