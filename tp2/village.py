class Village:
    def __init__(self, nom: str):
        self.nom = nom
        self.habitants = []

    def ajouter_habitant_composition(self, nom: str, age: int, adresse: str, animaux: dict = None):
        nouvel_habitant = Habitant(nom, age, adresse, animaux)
        self.habitants.append(nouvel_habitant)

    def ajouter_habitant_agregation(self, habitant: Habitant):
        self.habitants.append(habitant)

    def afficher_habitants(self):
        for habitant in self.habitants:
            print(f"- {habitant.get_nom()}, {habitant.age} ans")

    def get_habitants(self) -> list:
        return self.habitants


pytown = Village("PyTown")
# composition
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
# agregation
elise = Habitant("Élise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)

autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise)

assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()

# ajouter_habitant_composition illustre une relation de composition entre Village
# et Habitant, car le village crée et possède l'habitant. Si le village est
# détruit, l'habitant créé par composition n'existe plus ailleurs et disparaît
# avec lui.
# À l'inverse, ajouter_habitant_agregation illustre une relation d'agrégation,
# car le village utilise un habitant qui existe déjà indépendamment de lui, et
# qui peut être partagé par plusieurs villages (comme élise ici).