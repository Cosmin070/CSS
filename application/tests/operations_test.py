import unittest
from ..operations import summation


class OperationsTest(unittest.TestCase):

    def test_summation(self):
        self.assertEqual('7', summation('3','4'))
