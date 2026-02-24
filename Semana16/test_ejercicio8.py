import unittest
from Ejercicio8 import separar_primos

class TestEjercicio8(unittest.TestCase):

    def test_primos_1(self):
        # Arrange
        lista = [1, 2, 3, 4, 5]
        
        # Act
        resultado = separar_primos(lista)
        
        # Assert
        self.assertEqual(resultado, [2, 3, 5])

    def test_primos_2(self):
        # Arrange
        lista = [10, 11, 12, 13, 14]
        
        # Act
        resultado = separar_primos(lista)
        
        # Assert
        self.assertEqual(resultado, [11, 13])

    def test_primos_3(self):
        # Arrange
        lista = [17, 19, 23, 24, 25]
        
        # Act
        resultado = separar_primos(lista)
        
        # Assert
        self.assertEqual(resultado, [17, 19, 23])

if __name__ == "__main__":
    unittest.main()