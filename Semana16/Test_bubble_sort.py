import unittest
from bubble import bubble_sort  

class TestBubbleSort(unittest.TestCase):

    def test_small_list(self):
        """Funciona con una lista pequeña"""
        data = [5, 3, 8, 4, 2]
        result = bubble_sort(data, in_place=False)
        self.assertEqual(result, [2, 3, 4, 5, 8])

    def test_large_list(self):
        """Funciona con una lista grande (>100 elementos)"""
        data = list(range(200, 0, -1))  # de 200 a 1
        result = bubble_sort(data, in_place=False)
        self.assertEqual(result, list(range(1, 201)))

    def test_empty_list(self):
        """Funciona con una lista vacía"""
        data = []
        result = bubble_sort(data, in_place=False)
        self.assertEqual(result, [])

    def test_invalid_input(self):
        """No funciona con parámetros que no sean lista"""
        with self.assertRaises(TypeError):
            bubble_sort("not a list")
        with self.assertRaises(TypeError):
            bubble_sort(123)
        with self.assertRaises(TypeError):
            bubble_sort(None)

if __name__ == "__main__":
    unittest.main()