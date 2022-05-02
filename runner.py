from application.input_parser import parse
from application.arithmetic_tree import evaluate


def run():
    expression = parse("application/input.xml")
    print(evaluate(expression))


run()
