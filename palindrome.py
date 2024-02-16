import unittest
import string

def est_palindrome(chaine):
    whitelist = set(string.ascii_lowercase)
    chaine = chaine.lower()
    chaine = ''.join([char for char in chaine if char in whitelist])
    return chaine == chaine[::-1]
class TestEstPalindrome(unittest.TestCase):

    def test_palindrome_minuscules(self):
        self.assertTrue(est_palindrome("radar"))
    
    def test_palindrome_lol(self):
        self.assertTrue(est_palindrome("Able     was I ere I saw Elba"))

    def test_non_palindrome_minuscules(self):
        self.assertFalse(est_palindrome("python"))

    def test_palindrome_majuscules(self):
        self.assertTrue(est_palindrome("Able was I ere I saw Elba"))

    def test_non_palindrome_majuscules(self):
        self.assertFalse(est_palindrome("Palindrome"))

    def test_palindrome_espaces(self):
        self.assertTrue(est_palindrome("a man a plan a canal panama"))

    def test_non_palindrome_espaces(self):
        self.assertFalse(est_palindrome("not a palindrome"))

    def test_palindrome_personnalise_2(self):
        self.assertTrue(est_palindrome("À l'autel elle alla, elle le tua là"))


if __name__ == '__main__':
    unittest.main()