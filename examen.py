import unittest

def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

class TestEstPremier(unittest.TestCase):

    def test_nombres_non_premiers(self):
        non_premiers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 21, 22, 25, 27, 33]
        for nombre in non_premiers:
            with self.subTest(f"Testing {nombre}"):
                self.assertFalse(est_premier(nombre), f"{nombre} n'est pas un nombre premier.")

    def test_nombres_premiers(self):
        premiers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for nombre in premiers:
            with self.subTest(f"Testing {nombre}"):
                self.assertTrue(est_premier(nombre), f"{nombre} est un nombre premier.")

if __name__ == '__main__':
    unittest.main()