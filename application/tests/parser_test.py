import unittest
from application.input_parser import find_nth, get_symbols_position, parse, get_variables_and_values, get_expression, validate_tags
from ..exceptions import TagException

class ParserTest(unittest.TestCase):

    def test_find_nth(self):
        self.assertEqual(9, find_nth("<open_tag>something</open_tag>", ">", 1))
        self.assertEqual(18, find_nth("<another_tag>value</another_tag", "<", 2))
        self.assertEqual(11, find_nth("<tag>value</tag>", "/", 1))
        self.assertEqual(-1, find_nth("<tag>value</tag>", "/", 2))
        self.assertEqual(-1, find_nth("<tag>value</tag>", "^", 1))

    def test_get_symbols_position(self):
        open_bracket_positions, close_bracket_positions = get_symbols_position("<tag>value</tag>\n<another_tag>another_value</another_tag><tag>value</tag>")
        self.assertListEqual([0, 10, 17, 43, 57, 67], open_bracket_positions)
        self.assertListEqual([4, 15, 29, 56, 61, 72], close_bracket_positions)

    def test_parse(self):
        self.assertEqual("5+0", parse("application/tests/test_input.xml"))
        with self.assertRaises(TagException):
            parse("application/tests/test_input1.xml")
        with self.assertRaises(TagException):
            parse("application/tests/test_input2.xml")
        with self.assertRaises(TagException):
            parse("application/tests/test_input3.xml")
        with self.assertRaises(TagException):
            parse("application/tests/test_input4.xml")


    def test_get_variables_and_values(self):
        self.assertDictEqual({'a': '5', 'b': '0', 'expression': 'a+b'}, get_variables_and_values('<equation><expression>a+b</expression><a>4</a><a>5</a><b>0</b></equation>'))

    def test_get_expression(self):
        self.assertEqual("5+0", get_expression({'expression': 'a+b', 'a': '5', 'b': '0'}))
        self.failureException()