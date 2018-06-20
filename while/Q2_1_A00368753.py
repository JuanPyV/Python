import math

x = float(input("Dame la x: "))

if x <= -2:
    y = (x/2)+2
    print("El valor de y es: %d" % y)

elif x > -2 and x <= 0:
    y = x/(x+2)
    print("El valor de y es: %d" % y)

elif x > 0 and x <= 3:
    y = math.pow(x,2)+(4*x)+3
    print("El valor de y es: %d" % y)

else:
    y = math.sqrt(x-2)
    print("El valor de y es: %d" % y)






