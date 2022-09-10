import unittest
from interpreter.add import Add
from interpreter.subtract import Subtract
from interpreter.number import Number
from interpreter.conversion_context import ConversionContext


class TestUnit(unittest.TestCase):

    def test_add(self):
        result = Add(1, 2)
        self.assertEqual(str(result), '(1 Add 2)')

    def test_subtract(self):
        result = Subtract(7, 3)
        self.assertEqual(str(result), '(7 Subtract 3)')

    def test_number(self):
        result = Number('5')
        self.assertEqual(result, 5)

    def test_conversion_context(self):
        result = ConversionContext.parse_input('1 + 2 - 3')
        self.assertEqual(str(result), '((1 Add 2) Subtract 3)')





