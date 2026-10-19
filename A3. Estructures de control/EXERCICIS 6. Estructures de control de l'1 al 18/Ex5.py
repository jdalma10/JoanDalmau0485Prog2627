# 5. Escriu un programa que demani un nom d'usuari i una contrasenya i si s'ha introduït "anna" i "12345" 
# s'indica "Has entrat a sistema", sinó es dona un error.

nom_usuari = input("Introdueix el nom d'usuari:")
contrasenya = int(input ("Introdueix la contrasenya:"))

#if nom_usuari == 'anna' and contrasenya == '12345' or nom_usuari == 'manel' and contrasenya == '12345':
if (nom_usuari == 'anna' or nom_usuari == 'manel' ) and contrasenya == '12345':

    print ("Has accedit al sistema")
else:
    print("Error")