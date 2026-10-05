""" 17. Un ciclista part d'una ciutat A a les HH hores, MM minuts i SS segons. El temps de viatge fins arribar a una altra ciutat B és de T segons. 
Escriure un algoritme que determini l'hora d'arribada a la ciutat B. """


hh = int(input("Hores: "))
mm = int(input("Minuts: "))
ss = int(input("Segons: "))
ts = int(input("Temps(s): "))


total = hh * 3600 + mm * 60 + ss + ts

nh = total // 3600
nm = (total % 3600) // 60
ns = (total % 3600) % 60

print(f"{nh:02d}:{nm:02d}:{ns:02d}")

