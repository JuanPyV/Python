def valida_numero (mensaje):
    while True:
        try:
            dato = int(input(mensaje))
            if dato >= 1 and dato <= 10:
                return dato
            else:
                print("Fuera de rango")
        except ValueError:
            print("Dato invalido")



num = valida_numero("Ingresa numero: ")
print("ingresaste %d" %(num))
num = valida_numero("Ingresa otro numero: ")
print("ingresaste %d" %(num))