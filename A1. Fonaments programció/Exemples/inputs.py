nom = input("Diguem el teu nom: ")
edat = int(input("Diguem quants anys tens"))

#novaEdat = edat + 5     
# -> Es preferible fer una reassignació de variable 
#    si realment estic actualitzant-ne el valor.
edat = edat + 5

print(f"et dius {nom} i d'aqui 5 anys tindras {edat}")