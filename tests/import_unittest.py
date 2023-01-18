import unittest

from sample.calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_add_numbers(self):
        result = self.calc.add(2, 1)
        self.assertEqual(3, result)


if __name__ == '__main__':
    unittest.main()
