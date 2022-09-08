import unittest
from interpreter.conversion_context import ConversionContext


class TestUnit(unittest.TestCase):

    def test_expression(self):
        expression = "1 + 2 + 0 - 8"
        result = ConversionContext.parse_input(expression)
        self.assertEqual(str(result), '(((1 Add 2) Add 0) Subtract 8)')

    def test_output(self):
        expression = "1 + 2 + 0 - 8"
        result = ConversionContext.parse_input(expression)
        self.assertEqual(str(result.interpret()), '-5')
