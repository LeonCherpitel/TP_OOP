import unittest
from heritage import Habitant, Adulte, Enfant
from village import Village


class TestHabitant(unittest.TestCase):
    def setUp(self):
        self.h1 = Adulte("Aldric", "Jean", 25, "Rue A", {"vaches": 3})

    def test_age_setter_valide(self):
        self.h1.age = 26
        self.assertEqual(self.h1.age, 26)

    def test_age_setter_invalide(self):
        with self.assertRaises(ValueError):
            self.h1.age = -5


class TestVillage(unittest.TestCase):
    def setUp(self):
        self.pytown = Village("PyTown")

    def test_ajout_composition(self):
        self.pytown.ajouter_habitant_composition("Aldric", "Jean", 25, "Rue A", {"vaches": 3})
        self.assertEqual(len(self.pytown.get_habitants()), 1)
        self.assertEqual(self.pytown.get_habitants()[0].get_nom(), "Aldric")

    def test_ajout_agregation_partage_entre_villages(self):
        elise = Adulte("Elise", "Marie", 28, "Rue B", {"poules": 10})
        autre_village = Village("VillageVoisin")

        self.pytown.ajouter_habitant_agregation(elise)
        autre_village.ajouter_habitant_agregation(elise)

        self.assertIn(elise, self.pytown.get_habitants())
        self.assertIn(elise, autre_village.get_habitants())


class TestHeritage(unittest.TestCase):

    def test_retraite_adulte_coherente(self):
        adulte = Adulte("Dupont", "Marie", 35, "Rue A")
        self.assertEqual(adulte.calcul_nombre_annee_avant_retraite(), 27)

    def test_retraite_enfant_coherente(self):
        enfant = Enfant("Martin", "Lucas", 12, "Rue B")
        self.assertIn("enfant", enfant.calcul_nombre_annee_avant_retraite())

    def test_enfant_age_invalide(self):
        with self.assertRaises(ValueError):
            Enfant("Oups", "Test", 20, "Rue C")


if __name__ == "__main__":
    unittest.main(verbosity=2)