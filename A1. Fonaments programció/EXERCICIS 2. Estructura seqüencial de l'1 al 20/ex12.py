""" 12. Demana a l'usuari dos parells de nombres x1, y1 i x2, y2, que representin dos punts en el pla. 
Calcula i mostra la distància entre ells.
 """

c1X = int(input("X1: "))
c1Y = int(input("Y1: "))

c2X = int(input("X2: "))
c2Y = int(input("Y2: "))



distBase =  c2X - c1X
distAltura = c2Y - c1Y



distancia = (distBase**2 + distAltura**2)**0.5

print(distancia)