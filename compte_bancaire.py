import unittest

class CompteBancaire:

    def __init__(self, solde_initial):
        self.solde = solde_initial

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if self.solde < montant:
            raise ValueError("Solde insuffisant")
        self.solde -= montant

    def obtenir_solde(self):
        return self.solde

class TestCompteBancaire(unittest.TestCase):

    def test_deposer(self):
        compte = CompteBancaire(100)
        compte.deposer(50)
        self.assertEqual(compte.obtenir_solde(), 150, "Le solde après dépôt doit être de 150.")

    def test_retirer_solde_suffisant(self):
        compte = CompteBancaire(100)
        compte.retirer(30)
        self.assertEqual(compte.obtenir_solde(), 70, "Le solde après retrait doit être de 70.")

    def test_retirer_solde_insuffisant(self):
        compte = CompteBancaire(100)
        with self.assertRaises(ValueError):
            compte.retirer(150)

    def test_obtenir_solde_initial(self):
        compte = CompteBancaire(200)
        self.assertEqual(compte.obtenir_solde(), 200, "Le solde initial doit être de 200.")

if __name__ == '__main__':
    unittest.main()