print("Conversor de pies a yardas, pulgadas, centimetros y metros\n")

ft = float(input("Ingresa la medida en pies: "))

cm = ft*30.48

m = ft*.304

# Esto convierte de pulgadas a pies
inch = ft*12


yrd = ft*.333

print(" %.2f pies es equivalente a %.2f centimetros" % (ft, cm))
print(" %.2f pies es equivalente a %.2f metros" % (ft, m))
print(" %.2f pies es equivalente a %.2f pulgadas" % (ft, inch))
print(" %.2f pies es equivalente a %.2f yardas" % (ft, yrd))

# Autor: JuanPabloVelazco
