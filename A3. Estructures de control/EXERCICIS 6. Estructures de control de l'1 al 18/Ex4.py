# 4. Crea un programa que demani a l'usuari dos nombres i mostri la seva divisió si el segon no és zero,
#  o un missatge d'avís en cas contrari.

num1 = int(input("Introdueix el primer numero: "))
num2 = int(input("introdueix el segon numero: "))

if num2 == 0:
    print("No es pot dividir entre 0")
else: 
    print(num1 / num2)