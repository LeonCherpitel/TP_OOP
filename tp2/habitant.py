class Habitant:
    def __init__(self, nom: str, age: int, adresse: str, animaux: dict = None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux if animaux is not None else {}

    def affichage_adresse(self):
        print(f"{self.nom} habite à {self.adresse}")

    def compte_animal(self, animal: str) -> int:
        return self.animaux.get(animal, 0)
    

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"