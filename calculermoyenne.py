import unittest

def calculer_moyenne(liste):
    if not liste:
        raise ValueError("La liste ne doit pas être vide.")
    return sum(liste) / len(liste)

class TestCalculerMoyenne(unittest.TestCase):

    def test_liste_non_vide(self):
        self.assertEqual(calculer_moyenne([1, 2, 3, 4, 5]), 3.0)

    def test_liste_un_element(self):
        self.assertEqual(calculer_moyenne([7]), 7.0)

    def test_liste_negatifs(self):
        self.assertEqual(calculer_moyenne([-1, -2, -3, -4, -5]), -3.0)

    def test_liste_decimaux(self):
        self.assertAlmostEqual(calculer_moyenne([1.5, 2.5, 3.5]), 2.5, places=1)

    def test_liste_vide(self):
        with self.assertRaises(ValueError):
            calculer_moyenne([])

if __name__ == '__main__':
    unittest.main()