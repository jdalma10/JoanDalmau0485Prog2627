""" 10. Un alumne vol saber quin serà el seu qualificació final en la matèria de Algorismes. Aquesta qualificació es compon dels següents percentatges:
55% de la mitjana dels seus tres qualificacions parcials.
30% de la qualificació de l'examen final.
15% de la qualificació d'un treball final. """

p1 = float(input("parcial1: "))
p2 = float(input("parcial2: "))
p3 = float(input("parcial3: "))
ex = float(input("examen: "))
treball = float(input("treball: "))

notaMitjanaPArcials = (p1 +p2 + p3)/3
notaPArcials = notaMitjanaPArcials * 0.55
notaEx = ex*0.3 
notaTreball = treball*0.15
notaFinal = notaPArcials + notaEx + notaFinal

notaFinal = ((p1 +p2 + p3)/3)*0.55 + ex*0.3 + treball*0.15