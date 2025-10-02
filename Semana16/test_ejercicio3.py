import unittest
import Ejercicio3  

class TestEjercicio3(unittest.TestCase):

    def test_cambiar_variable_1(self):
        # Arrange
        Ejercicio3.Variable_global = 14
        
        # Act
        Ejercicio3.cambiar_variable()
        
        # Assert
        self.assertEqual(Ejercicio3.Variable_global, 28)

    def test_cambiar_variable_2(self):
        # Arrange
        Ejercicio3.Variable_global = 0
        
        # Act
        Ejercicio3.cambiar_variable()
        
        # Assert
        self.assertEqual(Ejercicio3.Variable_global, 28)

    def test_cambiar_variable_3(self):
        # Arrange
        Ejercicio3.Variable_global = 100
        
        # Act
        Ejercicio3.cambiar_variable()
        
        # Assert
        self.assertEqual(Ejercicio3.Variable_global, 28)

if __name__ == "__main__":
    unittest.main()