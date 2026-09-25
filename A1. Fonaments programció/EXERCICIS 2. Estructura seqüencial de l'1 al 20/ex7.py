# 7. Realitza un programa que rebi una quantitat de minuts i mostri per pantalla a quantes hores i minuts correspon.
 # Per exemple: 1000 minuts són 16 hores i 40 minuts.

minuts = int (input ("Minuts: "))

hores = minuts//60
minutsRestants = minuts%60

print(f"{hores} hora i {minutsRestants} minuts")

