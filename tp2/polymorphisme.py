def __str__(self):
    return f"{self.prenom} {self.nom}, {self.age} ans, habite à {self.adresse}"

def affichage(h: Habitant):
    """Fonction qui affiche un habitant"""
    print(str(h))

adulte = Adulte("Dupont", "Marie", 35, "123 Rue de la Paix")
print(adulte) 
affichage(adulte) 