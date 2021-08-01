from unittest import TestCase
from Lab02.conversion import from_decimal, to_decimal


class TestConversion(TestCase):
    def test_from_decimal(self):
        # normal
        self.assertEqual(from_decimal(250, 2), '11111010')
        self.assertEqual(from_decimal(0, 10), '0')
        self.assertEqual(from_decimal(12, 16), 'C')
        self.assertEqual(from_decimal(2553, 26), '3K5')
        # error
        self.assertEqual(from_decimal(-27, 2), 'Error: negative number')
        self.assertEqual(from_decimal(15, -10), 'Error: negative base')
        self.assertEqual(from_decimal(12, 37), 'Error: base > 36')
        self.assertEqual(from_decimal(12, 1), 'Error: base < 2')

    def test_to_decimal(self):
        # normal
        self.assertEqual(to_decimal("100", 2), 4)
        self.assertEqual(to_decimal("11", 5), 6)
        self.assertEqual(to_decimal("A", 16), 10)
        self.assertEqual(to_decimal("A", 12), 10)
        self.assertEqual(to_decimal("989", 10), 989)
        self.assertEqual(to_decimal("1BJ", 26), 981)
        self.assertEqual(to_decimal("1bj", 26), 981)
        # error
        self.assertEqual(to_decimal("56", 3), 'Error: incorrect number/base')
        self.assertEqual(to_decimal("191", 3), 'Error: incorrect number/base')
        self.assertEqual(to_decimal("-77", 6), 'Error: negative number')
        self.assertEqual(to_decimal("22", -9), 'Error: negative base')
        self.assertEqual(to_decimal("LOVE", 37), 'Error: base > 36')
        self.assertEqual(to_decimal("NOPE", 1), 'Error: base < 2')
