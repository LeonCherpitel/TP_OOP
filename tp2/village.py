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
            print(f"- {habitant.nom}, {habitant.age} ans")

pytown = Village("PyTown")
# composition
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
# agregation
elise = Habitant("Élise", 28, "Rue B", {"poules":10})
pytown.ajouter_habitant_agregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise)

#ajouter_habitants_composition illustre une relation de composition entre Village et Habitant, car le village crée et possède l'habitant. 
#Si le village est détruit, l'habitant créé par composition sera également détruit.
#à l'inverse, ajouter_habitants_agregation illustre une relation d'agrégation, car le village utilise un habitant qui existe déja. 