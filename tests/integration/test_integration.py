import time
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

    def test_timeout(self):
        time.sleep(10)
        expression = "1342 - 435 + 321 - 0 - 345 - 901 + 43 + 891 - 8945 + 7645 + 894 - 476 + 9 - 21 + 76 + 543"
        result = ConversionContext.parse_input(expression)
        self.assertEqual(str(result.interpret()), '641')


if __name__ == '__main__':
    unittest.main()