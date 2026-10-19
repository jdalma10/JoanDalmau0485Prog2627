# 8. Algorisme que demani dos nombres 'nota' i 'edat' i un caràcter 'sexe' i mostri el missatge 'ACCEPTADA'
#  si la nota és major o igual a cinc, l'edat és més gran o igual a divuit i el sexe és 'F'. 
# En cas que es compleixi el mateix, però el sexe sigui 'M', ha imprimir 'POSSIBLE'.
#  Si no es compleixen aquestes condicions s'ha de mostrar 'NO ACCEPTADA'.

nota = int(input("Escriu la nota"))
edat = int(input("Escriu la teva edat"))
sexe = input("Escriu 'F' si el teu sexe es femeni o 'M' si es masculi")

# if nota >= 5 and edat >= 18 and sexe == "F":
#     print("ACCEPTADA")
# elif nota >= 5 and edat >= 18 and sexe == "M":
#     print("POSSIBLE")
# else:
#     print("NO ACCEPTADA")

if nota >= 5 and edat >= 18:
    if sexe == "F":
        print("ACCEPTADA")
    elif  sexe == "M":
        print("POSSIBLE")
    else:
        print("ERROR; sexe incorrecte")
else:
    print("NO ACCEPTADA")

