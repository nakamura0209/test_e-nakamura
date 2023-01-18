import unittest

from sample.calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_add_numbers(self):
        result = self.calc.add(2, 1)
        self.assertEqual(3, result)

    def test_minus(self):
        self.assertEqual(self.calc.minus(1, 1), 0)
        self.assertTrue(self.calc.minus(2, 2) == 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(2, 2), 4)
        self.assertTrue(self.calc.multiplication(3, 3) == 9)


if __name__ == '__main__':
    unittest.main()
