#from audioop import add
import unittest
from interpreter.add import Add
from interpreter.subtract import Subtract
from interpreter.number import Number
from interpreter.conversion_context import ConversionContext


class TestUnit(unittest.TestCase):

    def test_add(self):
        result = Add(1, 2)
        self.assertEqual(str(result), '(1 Add 2)')

    def test_add_combined1(self):
        result = Add('(1 Add 2)',3)
        self.assertEqual(str(result), '((1 Add 2) Add 3)')

    def test_add_combined2(self):
        result = Add(5,'(3 Add -1)')
        self.assertEqual(str(result), '(5 Add (3 Add -1))')

    def test_subtract(self):
        result = Subtract(7, 3)
        self.assertEqual(str(result), '(7 Subtract 3)')

    def test_subtract_combined1(self):
        result = Subtract('(6 Subtract 2)',1)
        self.assertEqual(str(result), '((6 Subtract 2) Subtract 1)')

    def test_subtract_combined2(self):
        result = Subtract(4,'(2 Subtract -1)')
        self.assertEqual(str(result), '(4 Subtract (2 Subtract -1))')

    def test_mixed_combined1(self):
        result = Add('(3 Subtract 2)',1)
        self.assertEqual(str(result), '((3 Subtract 2) Add 1)')

    def test_mixed_combined2(self):
        result = Add(4,'(-1 Subtract 7)')
        self.assertEqual(str(result), '(4 Add (-1 Subtract 7))')

    def test_mixed_combined3(self):
        result = Subtract('(1 Add -2)',4)
        self.assertEqual(str(result), '((1 Add -2) Subtract 4)')

    def test_mixed_combined4(self):
        result = Subtract(3,'(1 Add 7)')
        self.assertEqual(str(result), '(3 Subtract (1 Add 7))')

    def test_number(self):
        result = Number('5')
        self.assertEqual(str(result), '5')

    def test_conversion_context(self):
        result = ConversionContext.parse_input('1 + 2 - 3')
        self.assertEqual(str(result), '((1 Add 2) Subtract 3)')



