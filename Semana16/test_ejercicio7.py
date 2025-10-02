import unittest
from Ejercicio7 import alphabetics_words

class TestEjercicio7(unittest.TestCase):

    def test_alphabetics_1(self):
        # Arrange
        texto = "python-variable-funcion-computadora-monitor"
        
        # Act
        resultado = alphabetics_words(texto)
        
        # Assert
        self.assertEqual(resultado, "computadora-funcion-monitor-python-variable")

    def test_alphabetics_2(self):
        # Arrange
        texto = "zebra-apple-banana"
        
        # Act
        resultado = alphabetics_words(texto)
        
        # Assert
        self.assertEqual(resultado, "apple-banana-zebra")

    def test_alphabetics_3(self):
        # Arrange
        texto = "delta-Alpha-charlie"
        
        # Act
        resultado = alphabetics_words(texto)
        
        # Assert
        self.assertEqual(resultado, "Alpha-charlie-delta")

if __name__ == "__main__":
    unittest.main()