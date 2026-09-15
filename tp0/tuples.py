# Exercice 3
# Question 1 

releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(releve): #création de la fonction
    nom_capteur = releve[0] #initialisation des valeurs
    valeur = releve[1]
    unite = releve[2]
    return f"{nom_capteur} : {valeur} {unite}" #ne pas utiliser 
#print sinon cela crée une erreur d'assert, il faut mettre un 
#return (voir le code faus en dessous)

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "laser_avant : 2.35 m"

"""
def afficher_releve(releve):
for releve in releves:
nom_capteur = releve[0]
valeur = releve[1]
unite = releve[2]
print(f"{nom_capteur} : {valeur} {unite}")

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "laser_avant : 2.35 m"
"""

# Question 2 
def recalibrer(releves, nom_capteur, nouvelle_valeur):
    for i in range(len(releves)):
        if releves[i][0] == nom_capteur:
            # conversion du tuple en liste
            releve_liste = list(releves[i])
            # mod de la valeur
            releve_liste[1] = nouvelle_valeur
            # Recréation du tuple
            releves[i] = tuple(releve_liste)
    return releves

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3
