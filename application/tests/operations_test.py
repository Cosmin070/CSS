import unittest
from unittest.mock import MagicMock, Mock
from application.operations import summation
from application.operations import power
from application.operations import multiplication
from application.operations import is_smaller
from application.operations import subtraction
from application.operations import division
from application.operations import square_root

class OperationsTest(unittest.TestCase):

    def test_summation(self):
        self.assertEqual('0', summation('0', '0'))

    def test_summation_error(self):
        self.assertEqual('20', summation('7', '13'))

    def test_power(self):
        # testing the if cases with their posibilities
        self.assertEqual('0', power('0', '2'))
        self.assertEqual('1', power('1', '2'))
        self.assertEqual('0', power('0', '0'))
        self.assertEqual('10', power('10', '1'))
        self.assertEqual('36', power('6', '2'))
        power('6', '2')

        mpl = Mock()
        mpl.multiplication()
        mpl.side_effect = multiplication
        self.assertEqual('36', power('6', '2'))
        mpl.multiplication.assert_called_once()

        sum = Mock()
        sum.summation()
        sum.side_effect = summation
        sum.summation.assert_called_once()
        sum.summation.assert_any_call()


    def test_is_smaller(self):
        self.assertEqual(True, is_smaller('0', '2'))
        self.assertEqual(False, is_smaller('2', '0'))
        self.assertEqual(True, is_smaller('15263123', '24185296431852615631561563'))
        self.assertEqual(False, is_smaller('24185296431852615631561563', '15263123'))
