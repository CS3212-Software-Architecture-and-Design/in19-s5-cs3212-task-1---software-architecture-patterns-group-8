import unittest
from interpreter.add import Add
from interpreter.subtract import Subtract
from interpreter.number import Number
from interpreter.conversion_context import ConversionContext
from interpreter.validation import Validation


class TestUnit(unittest.TestCase):

    def test_add(self):
        result = Add(1, 2)
        self.assertEqual(str(result), '(1 Add 2)')

        result = Add(0, 0)
        self.assertEqual(str(result), '(0 Add 0)')

        result = Add(-7, -8)
        self.assertEqual(str(result), '(-7 Add -8)')

        result = Add(0, 5)
        self.assertEqual(str(result), '(0 Add 5)')

        result = Add(0, -1)
        self.assertEqual(str(result), '(0 Add -1)')

        result = Add(5, 0)
        self.assertEqual(str(result), '(5 Add 0)')

        result = Add(-5, 0)
        self.assertEqual(str(result), '(-5 Add 0)')

        result = Add(-5, 8)
        self.assertEqual(str(result), '(-5 Add 8)')

    def test_subtract(self):
        result = Subtract(7, 3)
        self.assertEqual(str(result), '(7 Subtract 3)')

        result = Subtract(7, -3)
        self.assertEqual(str(result), '(7 Subtract -3)')

        result = Subtract(7, 0)
        self.assertEqual(str(result), '(7 Subtract 0)')

        result = Subtract(-7, 0)
        self.assertEqual(str(result), '(-7 Subtract 0)')

        result = Subtract(0, 3)
        self.assertEqual(str(result), '(0 Subtract 3)')

        result = Subtract(-3, 3)
        self.assertEqual(str(result), '(-3 Subtract 3)')

        result = Subtract(-3, 7)
        self.assertEqual(str(result), '(-3 Subtract 7)')

        result = Subtract(0, 0)
        self.assertEqual(str(result), '(0 Subtract 0)')

    def test_number(self):
        result = Number('5')
        self.assertEqual(str(result), '5')

        result = Number('-5')
        self.assertEqual(str(result), '-5')

        result = Number('0')
        self.assertEqual(str(result), '0')

    def test_validation(self):
        result = Validation.validate("1 + 5 -12")
        self.assertEqual(result,['1','+','5','-','12'])

        result = Validation.validate("1-10+234")
        self.assertEqual(result,['1','-','10','+','234'])

        result = Validation.validate('1')
        self.assertEqual(result,['1'])

        result = Validation.validate('2++3 ')
        self.assertEqual(result,False)

        result = Validation.validate('2+ ')
        self.assertEqual(result, False)

        result = Validation.validate(' ')
        self.assertEqual(result, False)

        result = Validation.validate("S+ 4-8")
        self.assertEqual(result, ['S','+','4','-','8'])












