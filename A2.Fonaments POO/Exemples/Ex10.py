#Demana una frase (amb espais sobrants al principi i al final), elimina'ls i mostra la frase neta i quantes paraules té.
frase = input("Posa una frase: ")

# Eliminar espais -> strip
frase = frase.strip()

# Dividir per paraule -> split

paraules = frase.split(" ")

print(len(paraules))