"""14. Donat un nombre de dues xifres, dissenyi un algoritme que permeti obtenir el nombre invertit. 
Exemple, si s'introdueix 23 que mostri 32."""

num = int(input("Posa un nombre de dos xifres: "))

unitats = num%10
desenes = num // 10

resultat = unitats * 10 + desenes

print (resultat)