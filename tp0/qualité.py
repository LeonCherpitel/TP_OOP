# Exercice 6


coefficients_terrain = { #initialisation des coeff du terrain
    "R": 1.0,  
    "H": 1.5,  
    "S": 2.0,  
}
coefficient_inconnu = 3.0


def cout_deplacement_propre(type_terrain, x_depart, y_depart, x_arrivee, y_arrivee):
 
    distance = ((x_arrivee - x_depart) ** 2 + (y_arrivee - y_depart) ** 2) ** 0.5 #norme euclidienne
    coefficient = coefficients_terrain.get(type_terrain, coefficient_inconnu)
    return distance * coefficient

#le cout est la distance entre le point de départ et le point d'arrvée en fct 
# du type de terrain traversé ou du coefficient inconnu si le type de terrain 
# n'est pas repertorié

#les problèmes du code non modifié sont que le code ne prend pas en compte les types de terrain non repertoriés et qu'il ne calcule pas correctement 
# le cout de déplacement. Le code modifié corrige ces problèmes en utilisant la méthode get() pour récupérer le coefficient du terrain et en calculant 
# correctement la distance entre les points de départ et d'arrivée. De plus, les noms et paramètres n'étaient pas explicites (d,t...etc) et ont été modifiés 
# pour être plus clairs (x_depart, y_depart, x_arrivee, y_arrivee).