import unittest
from application.operations import summation


class OperationsTest(unittest.TestCase):

    def test_summation(self):
         self.assertEqual('7', summation('3', '4'))

    def test_summation_error(self):
        self.assertEqual('20', summation('7','13'))
