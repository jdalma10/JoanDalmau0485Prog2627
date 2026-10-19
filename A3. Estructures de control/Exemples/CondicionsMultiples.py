edat = 22
es_estudiant = True
ciutat = "Lleida"

# Condicional compost
""" if edat >= 18 and (es_estudiant == True or ciutat == "Barcelona"):
    print("Ets major d'edat i ets estudiant o vius a Bcn.")
else:
    print("No compleixes les condicions.") """

# Separem el and amb un if/else
""" if edat >= 18:
    if es_estudiant or ciutat == "Barcelona":
        print("Ets major d'edat i ets estudiant o vius a Bcn.")
    else:
        print("No compleixes les condicions.") 
else:
    print("No compleixes les condicions.")  """


# Separem el or amb un elif.
if edat >= 18:
    if es_estudiant:
        print("Ets major d'edat i ets estudiant o vius a Bcn.")
    elif ciutat == "Barcelona":
        print("Ets major d'edat i ets estudiant o vius a Bcn.")
    else:
        print("No compleixes les condicions.") 
else:
    print("No compleixes les condicions.") 
