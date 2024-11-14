# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = Calculator()

    def test_add_7(self):
        # Test addition functionality
        result = self.calc.add_7(3, 7)
        self.assertEqual(result, 17)
        
        result = self.calc.add_7(-1, 1)
        self.assertEqual(result, 7)
        
        result = self.calc.add_7(-1, -1)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
