"""
Learning about unit testing!
Or add some lines of code
"""


import unittest
import calc


# TestCase has lots of method to use
class TestCalc(unittest.TestCase):

    # HAVE TO NAME PROPERLY
    # Has to start with "test_" or won't run
    # This is considered only one test with multiple checks
    def test_add(self):
        # Basic Case
        self.assertEqual(calc.add(10, 5), 15)
        # Testing Edge cases
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)


    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract (-1, 1), -2)
        self.assertEqual(calc.subtract (-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        # Update to check for floor division
        # If we had an error, add test to check for error
        self.assertEqual(calc.divide(5, 2), 2.5)

        # Testing for Error that we want
        # Passing arguments separately
        # self.assertRaises(ValueError, calc.divide, 10, 0)

        # Passing arguments the way you are used to
        # Use 'context manager'
        with self.assertRaises(ValueError):
            calc.divide(10,0)

if __name__ == '__main__':
    # This is required to run within editor
    # Or 'python -m unittest test_calc.py'

    unittest.main()
