from  interpreter.number import Number
from interpreter.add import Add
from interpreter.subtract import Subtract
from interpreter.validation import Validation


class ConversionContext:

    @classmethod
    def parse_input(cls, input_str):

        # input_array = input_str.split(" ")
        input_array = Validation.validate(input_str)
        if (not input_array):
            raise Exception("Please input valid expressions!")

        tree = []

        if(len(input_array)==1):
            return Number(input_array[0])

        while len(input_array) > 1:
            left = input_array.pop(0)
            left_expression = Number(left)
            operator = input_array.pop(0)
            right = input_array[0]
            right_expression = Number(right)

            if not tree:
                # Empty Data Structures return False by default
                if operator == '-':
                    tree.append(
                        Subtract(left_expression, right_expression))
                if operator == '+':
                    tree.append(
                        Add(left_expression, right_expression))
            else:
                if operator == '-':
                    tree.append(Subtract(tree[-1], right_expression))
                if operator == '+':
                    tree.append(Add(tree[-1], right_expression))

        return tree.pop()
