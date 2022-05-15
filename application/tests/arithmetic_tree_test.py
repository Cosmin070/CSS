import unittest
from application.arithmetic_tree import get_prio, get_result, compute_operation, check_next_char, check_close_parenthesis, check_parenthesis, evaluate


class OperationsTest(unittest.TestCase):

    def test_get_prio(self):
        self.assertEqual(1, get_prio('+'))
        self.assertEqual(2, get_prio('*'))
        self.assertEqual(3, get_prio('^'))
        self.assertEqual(0, get_prio(';'))
