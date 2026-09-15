# Exercice 7 

import unittest
from tuples import recalibrer
from ensembles import robots_double_mission, ajouter_robot_mission
from dictionnaires import consommer_piece, total_pieces


class TestJournalDeBord(unittest.TestCase):
    """Tests pour les fonctions sur les relevés (tuples)."""

    def setUp(self):
        """Prépare une liste de relevés utilisée par plusieurs tests."""
        self.releves = [
            ("laser_avant", 2.35, "m"),
            ("laser_arriere", 1.10, "m"),
            ("gyroscope", 87.5, "deg"),
        ]

    def test_recalibrer_capteur_existant(self):
        """Cas usuel : le capteur ciblé est bien présent dans la liste."""
        resultat = recalibrer(self.releves, "laser_avant", 2.40)
        self.assertEqual(resultat[0], ("laser_avant", 2.40, "m"))
        self.assertEqual(resultat[1], self.releves[1])
        self.assertEqual(resultat[2], self.releves[2])

    def test_recalibrer_capteur_absent(self):
        """Cas limite : le capteur demandé n'existe pas."""
        resultat = recalibrer(self.releves, "sonar", 1.0)
        self.assertEqual(resultat, self.releves)


class TestFlotteRobots(unittest.TestCase):
    """Tests pour les fonctions sur les missions des robots (ensembles)."""

    def setUp(self):
        """Prépare deux ensembles de robots utilisés par plusieurs tests."""
        self.robots_exploration = {"R2", "R5", "R7"}
        self.robots_transport = {"R5", "R9", "R7", "R3"}

    def test_robots_double_mission_cas_usuel(self):
        """Cas usuel : plusieurs robots sont affectés aux deux missions."""
        resultat = robots_double_mission(
            self.robots_exploration, self.robots_transport
        )
        self.assertEqual(resultat, {"R5", "R7"})

    def test_robots_double_mission_aucun_commun(self):
        """Cas limite : aucun robot en commun entre les deux missions."""
        resultat = robots_double_mission({"R1"}, {"R2"})
        self.assertEqual(resultat, set())

    def test_ajouter_robot_mission_nouveau_robot(self):
        """Cas usuel : ajout d'un robot absent de l'ensemble."""
        resultat = ajouter_robot_mission(self.robots_exploration, "R8")
        self.assertEqual(resultat, {"R2", "R5", "R7", "R8"})

    def test_ajouter_robot_mission_robot_deja_present(self):
        """Cas limite : le robot est déjà présent, pas de doublon créé."""
        resultat = ajouter_robot_mission(self.robots_exploration, "R5")
        self.assertEqual(resultat, {"R2", "R5", "R7"})
        self.assertEqual(len(resultat), 3)


class TestInventaire(unittest.TestCase):
    """Tests pour les fonctions sur le stock de pièces (dictionnaires)."""

    def setUp(self):
        """Prépare un stock de pièces utilisé par plusieurs tests."""
        self.pieces_stock = {
            "ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
            "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
        }

    def test_consommer_piece_cas_usuel(self):
        """Cas usuel : consommation d'une quantité disponible en stock."""
        consommer_piece(self.pieces_stock, "ModeleA", "moteurs", 3)
        self.assertEqual(self.pieces_stock["ModeleA"]["moteurs"], 7)

    def test_consommer_piece_stock_insuffisant(self):
        """Cas limite : quantité demandée supérieure au stock disponible."""
        with self.assertRaises(ValueError):
            consommer_piece(self.pieces_stock, "ModeleB", "roues", 100)

    def test_total_pieces_cas_usuel(self):
        """Cas usuel : plusieurs modèles avec des pièces à additionner."""
        totaux = total_pieces(self.pieces_stock)
        self.assertEqual(
            totaux, {"moteurs": 16, "capteurs": 40, "roues": 64}
        )

    def test_total_pieces_stock_vide(self):
        """Cas limite : aucun modèle dans le stock."""
        totaux = total_pieces({})
        self.assertEqual(
            totaux, {"moteurs": 0, "capteurs": 0, "roues": 0}
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)