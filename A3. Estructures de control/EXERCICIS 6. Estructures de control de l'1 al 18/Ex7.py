""" #7. Realitza un algoritme que calculi la potència, per això demana per teclat la base i l'exponent. Poden ocórrer tres coses:
L'exponent sigui positiu, només has d'imprimir la potència.
L'exponent sigui 0, el resultat es 1.
L'exponent sigui negatiu, el resultat es 1 / potència amb l'exponent positiu. """

b = float(input(f"posa la base: "))
e = int(input(f"posa l'exponent: "))
if e > 0:
    resultat = b ** e
    print(resultat)
elif e == 0:
    print(f"1")
else:
    resultat = 1 / (b ** abs(e))
    print(F"el resutat es: {resultat}")
