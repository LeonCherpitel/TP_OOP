# TP Programmation Orientée Objet - Guide Complet

## Structure du Projet

Ce projet contient une série d'exercices progressifs sur la programmation en Python, couvrant les structures de données, les opérations sur les ensembles, la programmation orientée objet, et les tests unitaires.

---

## TP0 - Fondamentaux Python

### Exercice 3 : Tuples et Relevés de Capteurs
**Fichier** : [tp0/tuples.py](tp0/tuples.py)

**Objectif** : Manipuler les tuples pour gérer des relevés de capteurs de robot.

**Contenu** :
- Création et indexation de tuples
- Fonction `afficher_releve()` : Affiche les données d'un capteur au format `"nom : valeur unité"`
- Fonction `recalibrer()` : Modifie la valeur d'un capteur spécifique

**Concepts clés** :
- Les tuples sont immuables → conversion en liste pour modification puis reconversion
- Utilisation d'assertions pour valider le comportement
- Manipulation de structures hétérogènes

**Capteurs utilisés** :
- Laser avant (2.35 m)
- Laser arrière (1.10 m)
- Gyroscope (87.5 deg)

---

### Exercice 4 : Ensembles et Missions Robotiques
**Fichier** : [tp0/robots.py](tp0/robots.py)

**Objectif** : Utiliser les ensembles pour gérer l'affectation de robots à différentes missions.

**Contenu** :
- Opérations sur les ensembles : intersection (`&`), union (`|`), différence (`-`)
- Fonction `ajouter_robot_mission()` : Ajoute un robot à une mission
- Fonction `retirer_robot_mission()` : Retire un robot d'une mission

**Opérations principales** :
| Opération | Symbole | Résultat | Exemple |
|-----------|---------|----------|---------|
| Intersection | `&` | Robots en double mission | `{"R5", "R7"}` |
| Union | `\|` | Tous les robots | `{"R2", "R3", "R5", "R7", "R9"}` |
| Différence | `-` | Robots exploration uniquement | `{"R2"}` |

**Robots** :
- R2, R3, R5, R7, R9

---

### Exercice 5 : Dictionnaires et Gestion de Stock
**Fichier** : [tp0/dictionnaires.py](tp0/dictionnaires.py)

**Objectif** : Gérer l'inventaire des pièces de différents modèles de robots.

**Contenu** :
- Structure de données imbriquée (dictionnaire de dictionnaires)
- Fonction `quantite_piece()` : Récupère la quantité d'une pièce pour un modèle
- Fonction `consommer_piece()` : Diminue le stock disponible
- Fonction `ajouter_modele()` : Crée un nouveau modèle de robot avec ses pièces
- Fonction `total_pieces()` : Calcule le stock total de chaque type de pièce

**Modèles disponibles** :
- ModeleA : 10 moteurs, 25 capteurs, 40 roues
- ModeleB : 6 moteurs, 15 capteurs, 24 roues
- ModeleC : 4 moteurs, 10 capteurs, 16 roues

**Pièces gérées** : moteurs, capteurs, roues

---

### Exercice 6 : Qualité de Code et Calcul de Déplacement
**Fichier** : [tp0/qualité.py](tp0/qualité.py)

**Objectif** : Améliorer la qualité du code en optimisant la lisibilité et la robustesse.

**Contenu** :
- Fonction `cout_deplacement_propre()` : Calcule le coût de déplacement d'un robot
- Distance euclidienne basée sur les coordonnées (x, y)
- Coefficients de terrain pour différents types de surface

**Formule** :
```
Coût = distance × coefficient_terrain
distance = √[(x_arrivée - x_départ)² + (y_arrivée - y_départ)²]
```

**Coefficients de terrain** :
- R (Route) : 1.0
- H (Herbe) : 1.5
- S (Sable) : 2.0
- Terrain inconnu : 3.0

**Améliorations apportées** :
- Noms de variables explicites (au lieu de `d`, `t`, etc.)
- Utilisation de `.get()` pour gérer les terrains non reconnus
- Commentaires explicatifs

---

### Exercice 7 : Tests Unitaires
**Fichier** : [tp0/tests.py](tp0/tests.py)

**Objectif** : Écrire des tests unitaires robustes pour valider les fonctions des exercices précédents.

**Contenu** :

#### TestJournalDeBord
Tests pour les fonctions de gestion des relevés (tuples) :
- `test_recalibrer_capteur_existant()` : Cas nominal
- `test_recalibrer_capteur_absent()` : Cas limite (capteur inexistant)

#### TestFlotteRobots
Tests pour les fonctions de gestion des missions robotiques :
- `test_robots_double_mission_cas_usuel()` : Plusieurs robots en commun
- `test_robots_double_mission_aucun_commun()` : Cas limite (aucun robot partagé)

**Framework utilisé** : `unittest`

**Bonnes pratiques** :
- Méthode `setUp()` pour initialiser les données de test
- Assertions explicites
- Cas usuels et cas limites couverts

---

### Exercice 8 : Utilisation de GitHub Copilot
**Fichier** : [tp0/IA.py](tp0/IA.py)

**Objectif** : Réflexion critique sur l'utilisation de l'IA dans le développement.

**Points discutés** :
- **Avantages** : Code plus concis et généralement bien organisé
- **Inconvénients** : 
  - Peut utiliser des constructions plus complexes que nécessaires
  - Peut générer du code difficile à comprendre pour un débutant
  - Peut faire des erreurs ou mal interpréter le contexte
- **Recommandation** : Toujours vérifier et comprendre le code généré

---

## Installation et Exécution

### Environnement Python

**Fichier de configuration** : `environment.yml`

Pour créer l'environnement :
```bash
conda env create -f environment.yml
conda activate tp_oop
```

### Exécution des tests

```bash
# Tests du TP0
python -m unittest tp0.tests
```

### Exécution des exercices individuels

```bash
python tp0/tuples.py
python tp0/robots.py
python tp0/dictionnaires.py
python tp0/qualité.py
```

---

## Concepts Abordés

| Concept | Exercices | Description |
|---------|-----------|-------------|
| **Tuples** | 3 | Collections immuables de données hétérogènes |
| **Ensembles** | 4 | Opérations mathématiques (union, intersection, différence) |
| **Dictionnaires** | 5 | Structures clé-valeur, imbrication, méthodes |
| **Qualité de code** | 6 | Lisibilité, documentation, robustesse |
| **Tests unitaires** | 7 | Framework unittest, cas nominaux et limites |

---

## Progression Recommandée

1. **Exercice 3** : Comprendre les tuples et la manipulation de structures immuables
2. **Exercice 4** : Découvrir les opérations sur les ensembles
3. **Exercice 5** : Approfondir les dictionnaires et structures imbriquées
4. **Exercice 6** : Refactoriser et améliorer la qualité du code
5. **Exercice 7** : Valider avec des tests robustes
6. **Exercice 8** : Réfléchir sur l'usage de l'IA

---

## Auteur

Travaux pratiques en Programmation Orientée Objet  
Année académique 2026-2027
