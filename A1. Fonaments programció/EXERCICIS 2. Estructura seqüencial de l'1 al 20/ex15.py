#15. Donades dues variables numèriques A i B, que l'usuari ha de teclejar, 
# es demana realitzar un algoritme que intercanviï els valors de les dues variables 
# i mostri que fa valen a al final les dues variables.

a = int(input("Posa a: "))
b = int(input("Posa b: "))


aux = a
a = b
b = aux

print(f"a: {a}")
print(f"b: {b}")

# Doble assignació
# a , b = b ,a 