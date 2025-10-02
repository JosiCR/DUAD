import unittest
from Ejercicio5 import vuelta

class TestEjercicio5(unittest.TestCase):

    def test_vuelta_1(self):
        # Arrange
        # Act
        resultado = vuelta()
        
        # Assert
        self.assertEqual(resultado, "odnum aloh")

    def test_vuelta_2(self):
        # Arrange
        my_string = "python"
        
        # Act
        resultado = ''.join(reversed(my_string))
        
        # Assert
        self.assertEqual(resultado, "nohtyp")

    def test_vuelta_3(self):
        # Arrange
        my_string = "12345"
        
        # Act
        resultado = ''.join(reversed(my_string))
        
        # Assert
        self.assertEqual(resultado, "54321")

if __name__ == "__main__":
    unittest.main()