from abc import ABC, abstractmethod


class Habitant(ABC):

    def __init__(self, nom: str, prenom: str, age: int, adresse: str, animaux: dict = None):
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}
        self.age = age

    def get_nom(self) -> str:
        return self.__nom

    def get_prenom(self) -> str:
        return self.__prenom

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

    def __str__(self):
        return f"{self.get_prenom()} {self.get_nom()}, {self.age} ans, habite a {self.get_adresse()}"

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        """calcule le nombre d'années restantes avant la retraite."""


class Adulte(Habitant):
    """classe représentant un adulte, héritant de la classe Habitant."""

    AGE_RETRAITE = 62

    def __init__(self, nom: str, prenom: str, age: int, adresse: str, animaux: dict = None):
        if age < 18:
            raise ValueError("adulte >= 18 ans")
        super().__init__(nom, prenom, age, adresse, animaux)

    def calcul_nombre_annee_avant_retraite(self):
        if self.age >= Adulte.AGE_RETRAITE:
            return "Deja a la retraite"
        return Adulte.AGE_RETRAITE - self.age


class Enfant(Habitant):
    def __init__(self, nom: str, prenom: str, age: int, adresse: str, animaux: dict = None):
        if age >= 18:
            raise ValueError("enfant < 18 ans")
        super().__init__(nom, prenom, age, adresse, animaux)

    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: un enfant ne peut pas calculer sa retraite"


def affichage(h: Habitant):
    print(str(h))


adulte = Adulte("Dupont", "Marie", 35, "Rue A")
enfant = Enfant("Martin", "Lucas", 12, "Rue B")

assert isinstance(adulte, Habitant)
assert adulte.calcul_nombre_annee_avant_retraite() == 27
assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()

try:
    Enfant("Oups", "Test", 25, "Rue C")
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass

affichage(adulte)
affichage(enfant)