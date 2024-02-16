def compter_mots(phrase):
    mots = phrase.split()
    return len(mots)

import unittest

class TestCompterMots(unittest.TestCase):

    def test_phrase_vide(self):
        self.assertEqual(compter_mots(""), 0)

    def test_phrase_avec_espaces(self):
        self.assertEqual(compter_mots("    "), 0)

    def test_phrase_un_mot(self):
        self.assertEqual(compter_mots("Bonjour"), 1)

    def test_phrase_plusieurs_mots(self):
        self.assertEqual(compter_mots("Il fait beau aujourd'hui"), 4)

    def test_phrase_espaces_supplementaires(self):
        self.assertEqual(compter_mots("   Bonjour    le   monde   "), 3)

    def test_phrase_caracteres_speciaux(self):
        phrase_speciale = "C'est l'été ! Comment ça va ?"
        self.assertEqual(compter_mots(phrase_speciale), 7)

if __name__ == '__main__':
    unittest.main()