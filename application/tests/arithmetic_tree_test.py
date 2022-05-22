import random
import unittest
from unittest.mock import patch
from application.arithmetic_tree import get_prio, get_result, compute_operation, check_next_char, check_close_parenthesis, check_parenthesis, evaluate


class OperationsTest(unittest.TestCase):

    def test_get_prio(self):
        self.assertEqual(1, get_prio('+'))
        self.assertEqual(2, get_prio('*'))
        self.assertEqual(3, get_prio('^'))

    @patch('application.arithmetic_tree.summation')
    def test_get_result_plus(self, get_content_mock):
        a = str(random.randint(1, 100000))
        b = str(random.randint(1, 100000))
        get_content_mock.return_value = 'mocked'
        self.assertEqual(get_result(a, b, '+'), 'mocked')
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()

    @patch('application.arithmetic_tree.subtraction')
    def test_get_result_minus(self, get_content_mock):
        a = str(random.randint(1, 100000))
        b = str(random.randint(1, 100000))
        get_content_mock.return_value = 'mocked'
        self.assertEqual(get_result(a, b, '-'), 'mocked')
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()

    @patch('application.arithmetic_tree.multiplication')
    def test_get_result_mul(self, get_content_mock):
        a = str(random.randint(1, 100000))
        b = str(random.randint(1, 100000))
        get_content_mock.return_value = 'mocked'
        self.assertEqual(get_result(a, b, '*'), 'mocked')
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()

    @patch('application.arithmetic_tree.division')
    def test_get_result_div(self, get_content_mock):
        a = str(random.randint(1, 100000))
        b = str(random.randint(1, 100000))
        get_content_mock.return_value = 'mocked'
        self.assertEqual(get_result(a, b, '/'), 'mocked')
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()

    @patch('application.arithmetic_tree.power')
    def test_get_result_pow(self, get_content_mock):
        a = str(random.randint(1, 100000))
        b = str(random.randint(1, 100000))
        get_content_mock.return_value = 'mocked'
        self.assertEqual(get_result(a, b, '^'), 'mocked')
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()

    @patch('application.arithmetic_tree.square_root')
    def test_get_result_sqr(self, get_content_mock):
        a = str(random.randint(1, 100000))
        b = str(random.randint(1, 100000))
        get_content_mock.return_value = 'mocked'
        self.assertEqual(get_result(a, b, '√'), 'mocked')
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()

    def test_compute_operation(self):
        n = 129
        n_1 = ''.join(["{}".format(random.randint(0, 9)) for temp in range(0, n)])
        n_2 = ''.join(["{}".format(random.randint(0, 9)) for temp in range(0, n)])
        operators = [n_1, n_2]
        operations = ['+']
        with self.assertRaises(Exception) as context:
            compute_operation(operators, operations)
        self.assertTrue('Number too large.' in str(context.exception))
        n = 11
        n_1 = ''.join(["{}".format(random.randint(0, 9)) for temp in range(0, n)])
        n_2 = ''.join(["{}".format(random.randint(0, 9)) for temp in range(0, n)])
        operators = [n_1, n_2]
        operations = ['*']
        with self.assertRaises(Exception) as context:
            compute_operation(operators, operations)
        self.assertTrue('Number too large for multiplication/division.' in str(context.exception))
        n_1 = ''.join(["{}".format(random.randint(0, 9)) for temp in range(0, n)])
        n_2 = ''.join(["{}".format(random.randint(0, 9)) for temp in range(0, n)])
        operators = [n_1, n_2]
        operations = ['^']
        with self.assertRaises(Exception) as context:
            compute_operation(operators, operations)
        self.assertTrue('Number too large for power.' in str(context.exception))

    @patch('application.arithmetic_tree.get_result')
    def test_compute_operation_mock_not_sqr(self, get_content_mock):
        get_content_mock.return_value = 'mocked'
        a = str(random.randint(1, 10000))
        b = str(random.randint(1, 10000))
        operators = [a, b]
        operations = ['+']
        compute_operation(operators, operations)
        self.assertEqual(operators, ['mocked'])
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()

    @patch('application.arithmetic_tree.get_result')
    def test_compute_operation_mock_sqr(self, get_content_mock):
        get_content_mock.return_value = 'mocked'
        a = str(random.randint(1, 10000))
        operators = [a]
        operations = ['√']
        compute_operation(operators, operations)
        self.assertEqual(operators, ['mocked'])
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()

    def test_check_close_parenthesis(self):
        self.assertEqual(False, check_close_parenthesis(['(', '+', ')']))
        self.assertEqual(True, check_close_parenthesis(['+', ')']))

    def test_check_parenthesis(self):
        self.assertEqual(False, check_parenthesis(['(', '+', ')']))
        self.assertEqual(True, check_parenthesis(['+', ')']))

    def test_check_next_char(self):
        self.assertEqual(True, check_next_char('    x+y', -1))
        self.assertEqual(False, check_next_char('10+25', -1))
        self.assertEqual(False, check_next_char('    (    10 +                 25 )', -1))

    def test_evaluate(self):
        with self.assertRaises(Exception) as context:
            evaluate('(      10 + 25 ))')
        self.assertTrue('The expression is INVALID. You can not close a parenthesis without to open one.' in str(context.exception))
        with self.assertRaises(Exception) as context:
            evaluate('(√√25)')
        self.assertTrue('The expression is INVALID. Operation without both or any operand.' in str(context.exception))
        with self.assertRaises(Exception) as context:
            evaluate('(10 +++ 10 )')
        self.assertTrue('The expression is INVALID. Operation without both or any operand.' in str(context.exception))
        with self.assertRaises(Exception) as context:
            evaluate('((10+10)')
        self.assertTrue('The expression is INVALID. Check parenthesis.' in str(context.exception))
        self.assertEqual('10', evaluate('(5+5)*5/5'))
