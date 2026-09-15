# Exercice 5 


pieces_stock = {
    "ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
    "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(pieces_stock, modele, piece):
    """Retourne la quantité disponible d'une pièce pour un modèle donné."""
    return pieces_stock[modele][piece]


assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

def consommer_piece(pieces_stock, modele, piece, quantite):
    """Retire une quantité de pièces du stock pour un modèle donné."""
    pieces_stock[modele][piece] = pieces_stock[modele][piece] - quantite


def ajouter_modele(pieces_stock, modele, moteurs, capteurs, roues):
    """Ajoute un nouveau modèle de robot avec son stock initial."""
    pieces_stock[modele] = {
        "moteurs": moteurs