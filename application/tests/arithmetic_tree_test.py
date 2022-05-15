import random
import unittest
from unittest.mock import Mock, patch
from application.arithmetic_tree import get_prio, get_result, compute_operation, check_next_char, check_close_parenthesis, check_parenthesis, evaluate


class OperationsTest(unittest.TestCase):

    def test_get_prio(self):
        self.assertEqual(1, get_prio('+'))
        self.assertEqual(2, get_prio('*'))
        self.assertEqual(3, get_prio('^'))
        self.assertEqual(0, get_prio(';'))

    @patch('application.arithmetic_tree.summation')
    def test_get_result(self, get_content_mock):
        get_content_mock.return_value = 'mocked'
        self.assertEqual(get_result(), 'mocked')
        self.assertEqual(get_content_mock.call_count, 1)
        get_content_mock.assert_called_once()
