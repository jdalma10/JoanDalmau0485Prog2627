class Alumne:
    def __init__(self, nom, dni):
        self.nom = nom
        self.dni = dni

    def __str__(self):
        return(f"{self.nom}, {self.dni}")  

    def saluda(self):
        print(f"Hola em dic {self.nom}")

alumne = Alumne("Joan", "333333333G")
alumne2 = Alumne("Maria", "333333333H")

# Accés a un atribut
print(alumne.nom, alumne.dni)

# Accés a un mètode
alumne2.saluda()


print(alumne2)