from interpreter.conversion_context import ConversionContext


class Demo:

    question_asked = str(input("Enter the expression: "))
    output = ConversionContext.parse_input(question_asked)
    print(output.interpret())


if __name__ == '__main__':
    Demo()
