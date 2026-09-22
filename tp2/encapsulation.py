class Habitant:
    def __init__(self, nom: str, age: int, adresse: str, animaux: dict = None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}

    def get_nom(self) -> str:
        return self.__nom

    def get_adresse(self) -> str:
        return self.__adresse

    def get_animaux(self) -> dict:
        return self.__animaux

    def set_nom(self, nom: str):
        self.__nom = nom

    def set_adresse(self, adresse: str):
        self.__adresse = adresse

    def set_animaux(self, animaux: dict):
        self.__animaux = animaux

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, valeur: int):
        if valeur < 0 or valeur > 130:
            raise ValueError("l'âge doit être compris entre 0 et 130")
        self.__age = valeur

    def affichage_adresse(self):
        print(f"{self.__nom} habite à {self.__adresse}")

    def compte_animal(self, animal: str) -> int:
        return self.__animaux.get(animal, 0)


h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

assert h1.get_nom() == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse()  # affiche "Aldric habite à Rue A"

h1.age = 26
assert h1.age == 26

try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass