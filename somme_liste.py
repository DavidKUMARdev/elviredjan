import unittest

def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

class TestSommeListe(unittest.TestCase):

    def test_liste_vide(self):
        self.assertEqual(somme_liste([]), 0, "La somme = 0.")

    def test_liste_positifs(self):
        self.assertEqual(somme_liste([1, 2, 3, 4, 5]), 15, "La somme = 15.")

    def test_liste_negatifs(self):
        self.assertEqual(somme_liste([-1, -2, -3, -4, -5]), -15, "La somme = -15.")

    def test_liste_mixte(self):
        self.assertEqual(somme_liste([1, -2, 3, -4, 5]), 3, "La somme = 3.")

if __name__ == '__main__':
    unittest.main()