import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import detectar_palindromo

class TestDetectarPalindromo(unittest.TestCase):
    def test_detectar_palindromo_palindromo(self):
        self.assertTrue(detectar_palindromo("radar"))

    def test_detectar_palindromo_no_palindromo(self):
        self.assertFalse(detectar_palindromo("python"))

    def test_detectar_palindromo_cadena_vacia(self):
        self.assertTrue(detectar_palindromo(""))

    def test_detectar_palindromo_con_caracteres_especiales(self):
        self.assertFalse(detectar_palindromo("¡Anita, lava la tina!"))

    def test_detectar_palindromo_con_numeros(self):
        self.assertTrue(detectar_palindromo("12321"))

if __name__ == '__main__':
    unittest.main()
