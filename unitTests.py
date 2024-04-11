import unittest
from calculator import Calculator

class (unittest):
    def __init__(self):
        self.c = Calculator.calculator

    def test_adder(self):
        result = self.c.add(2,2)
        expected = 4
        self.assertEqual(result, expected, "You did not add correctly, "
        "make sure to add 2 and 2 to make 4.")

    def test_subractor(self):
        result = self.c.subtract(2,2)
        expected = 0
        self.assertEqual(result,expected, "You did not subtract correctly, "
        "make sure to subtract 2 from 2 to make 0.")

        result = self.c.subtract(5,3)
        expected = 2
        self.assertEqual(result, expected)

    def test_history(self):
        self.assertEqual(len(self.c.history) , 0)
        
        self.c.add(3,5)
        self.assertEqual(len(self.c.history) , 1)
        self.assertEqual(self.c.history[0], ["3 + 5"])