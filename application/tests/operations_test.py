import unittest
from unittest.mock import MagicMock, Mock

from application.exceptions import DivisionByZeroException
from application.operations import summation, subtraction
from application.operations import power
from application.operations import multiplication
from application.operations import is_smaller
from application.operations import division
from application.operations import square_root


class OperationsTest(unittest.TestCase):

    def test_summation_error(self):
        self.assertEqual('20', summation('7', '13'))

    def test_power(self):
        # testing the if cases with their posibilities
        self.assertEqual('0', power('0', '2'))
        self.assertEqual('1', power('1', '2'))
        self.assertEqual('0', power('0', '0'))
        self.assertEqual('10', power('10', '1'))
        self.assertEqual('36', power('6', '2'))
        self.assertEqual('1', power('10', '0'))
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
        #self.assertEqual(sum.call_count, 2)

    def test_is_smaller(self):
        self.assertEqual(True, is_smaller('0', '2'))
        self.assertEqual(False, is_smaller('2', '0'))
        self.assertEqual(True, is_smaller('15263123', '24185296431852615631561563'))
        self.assertEqual(False, is_smaller('24185296431852615631561563', '15263123'))

    def test_multiplication(self):
        self.assertEqual('0', multiplication('0', '0'))
        self.assertEqual('121', multiplication('11', '11'))
        sum = Mock()
        sum.summation()
        sum.side_effect = summation
        sum.summation.assert_called_once()
        sum.summation.assert_any_call()

    def test_summatinon(self):
        self.assertEqual('12', summation('3', '9'))
        self.assertEqual('12', summation('9', '3'))
        self.assertEqual('0', summation('0', '0'))

    def test_subtraction(self):
        self.assertEqual('6', subtraction('3', '9'))
        self.assertEqual('6', subtraction('9', '3'))
        self.assertEqual('-6', subtraction('0', '6'))
        is_sml = Mock()
        is_sml.summation()
        is_sml.side_effect = summation
        is_sml.summation.assert_called_once()
        is_sml.summation.assert_any_call()
        # self.assertEqual(is_sml.call_count, 2)

    def test_division(self):
        self.assertEqual('0', division('0', '9'))
        with self.assertRaises(Exception) as context:
            division('9', '0')
        self.assertTrue('Division by 0.' in str(context.exception))
        self.assertEqual('3', division('12', '4'))

        subs = Mock()
        subs.summation()
        subs.side_effect = summation
        subs.summation.assert_called_once()
        subs.summation.assert_any_call()

        sum = Mock()
        sum.summation()
        sum.side_effect = summation
        sum.summation.assert_called_once()
        sum.summation.assert_any_call()

    def test_square_root(self):
        self.assertEqual('3', square_root('9'))
        self.assertEqual('0', square_root('0'))
        self.assertEqual('1', square_root('1'))
        with self.assertRaises(Exception) as context:
            square_root('-9')
        self.assertTrue('Negative number.' in str(context.exception))