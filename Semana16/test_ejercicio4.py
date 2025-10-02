import unittest
from Ejercicio4 import sumar

class TestEjercicio4(unittest.TestCase):

    def test_sumar_1(self):
        # Arrange
        lista = [1, 2, 3, 4, 5]
        
        # Act
        resultado = sumar(lista)
        
        # Assert
        self.assertEqual(resultado, 15)

    def test_sumar_2(self):
        # Arrange
        lista = [-1, -2, -3]
        
        # Act
        resultado = sumar(lista)
        
        # Assert
        self.assertEqual(resultado, -6)

    def test_sumar_3(self):
        # Arrange
        lista = []
        
        # Act
        resultado = sumar(lista)
        
        # Assert
        self.assertEqual(resultado, 0)

if __name__ == "__main__":
    unittest.main()