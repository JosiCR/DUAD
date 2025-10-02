import unittest
from Ejercicio6 import contador_lower_upper

class TestEjercicio6(unittest.TestCase):

    def test_contador_1(self):
        # Arrange
        texto = "I also Love Sushi"
        
        # Act
        resultado = contador_lower_upper(texto)
        
        # Assert
        self.assertEqual(resultado, (3, 11))

    def test_contador_2(self):
        # Arrange
        texto = "HELLO world"
        
        # Act
        resultado = contador_lower_upper(texto)
        
        # Assert
        self.assertEqual(resultado, (5, 5))

    def test_contador_3(self):
        # Arrange
        texto = "1234!"
        
        # Act
        resultado = contador_lower_upper(texto)
        
        # Assert
        self.assertEqual(resultado, (0, 0))

if __name__ == "__main__":
    unittest.main()