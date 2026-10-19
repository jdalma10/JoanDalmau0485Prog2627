# 1. Algorisme que demani dos nombres i indiqui si el primer és més gran que el segon o no.

num1 = int(input("Introdueix el numero"))
num2 = int(input("Introdueix un altre numero"))

if num1 > num2:
    print("N1 mes gran")
elif num1 < num2:
    print(" N1 mes petit")
else:
    print("iguals")