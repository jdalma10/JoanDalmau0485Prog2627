#7. Comptar una lletra


nom = input("Posa el teu nom: ")
lletra = input("Lletra a buscar: ")
nomMinus = nom.lower()
print(f"La lletra  {lletra} surt {nomMinus.count(lletra)}")