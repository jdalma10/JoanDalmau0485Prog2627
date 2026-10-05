d = float(input("Distància entre els vehicles (km): "))
v1 = float(input("Velocitat del vehicle de darrere (km/h): "))
v2 = float(input("Velocitat del vehicle de davant (km/h): "))

temps_h = d / (v1 - v2)      # temps en hores
temps_min = temps_h * 60     # temps en minuts
print(f"Es trobaran en {temps_min:.2f} minuts.")

