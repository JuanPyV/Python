
x = (float(input("Dame el valor de la x: ")))

if x <= -1:

    r = 2*x

    print("La x vale %.2f" % r)
else:
    if x > -1 and x < 1:

        r = (2*x)+1

        print("La x vale %.2f" % r)

    else:
        if x >= 1 and x < 4:

            r = (-x)+4

            print("La x vale %.2f" % r)

        else:
            if x >= 4:

                r = x - 1

                print("La x vale %.2f" % r)
