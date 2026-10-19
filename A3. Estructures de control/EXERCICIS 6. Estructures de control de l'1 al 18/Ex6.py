# Programa que llegeixi una lletra per teclat i 
# comprovi si és una lletra majúscula.

lletra = input("Introdueix una lletra: ")

if lletra[0].isdigit() == False:
    if lletra[0] == lletra[0].upper():
        print("La lletra es majuscula.")
    else: 
        print("La lletra es minuscula.")
else:
    print("ERROR; és un número.")

