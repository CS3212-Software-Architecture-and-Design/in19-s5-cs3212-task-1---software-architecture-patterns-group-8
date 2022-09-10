from interpreter.expression import Expression


class Number(Expression):
    """Terminal Expression"""

    def __init__(self, value):
        self.value = int(value)

    def get_value(self):
        return self.value

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)
