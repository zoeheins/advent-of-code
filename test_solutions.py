import unittest
from solutions import day1


class TestDayOne(unittest.TestCase):

    def test_returns_sum(self):
        result = day1.solve('1122')
        self.assertEqual(result, 3)

    def test_returns_zero(self):
        result = day1.solve('1234')
        self.assertEqual(result, 0)

