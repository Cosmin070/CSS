from application.operations import summation, subtraction, power, multiplication, division, square_root
from application.exceptions import LargeNumberException, InvalidExpressionException


def get_prio(operand):
    assert operand in ['+', '-', '*', '/', '^', '√', '(', ')']
    if operand == '+' or operand == '-':
        return 1
    if operand == '*' or operand == '/':
        return 2
    if operand == '√' or operand == '^':
        return 3
    return 0


def get_result(a, b, operand):
    assert type(a) == str
    assert type(b) == str
    assert operand in ['+', '-', '*', '/', '^', '√']
    if operand == '+':
        return summation(a, b)
    if operand == '-':
        return subtraction(a, b)
    if operand == '*':
        return multiplication(a, b)
    if operand == '/':
        return division(a, b)
    if operand == '^':
        return power(a, b)
    if operand == '√':
        return square_root(a)


def compute_operation(operands, operations):
    assert all([type(op) == str for op in operations])
    assert all([type(op) == str for op in operands])
    if not all(len(x) < 128 for x in operands):
        raise LargeNumberException("Number too large.")
    if operations[-1] != '√':
        val2 = operands.pop()
        val1 = operands.pop()
        op = operations.pop()
        if op in '*/' and ((len(val1) + len(val2) >= 8 and abs(len(val1) - len(val2)) < 3)
                           or (len(val1) + len(val2) > 20)):
            raise LargeNumberException("Number too large for multiplication/division.")
        if op == "^" and (len(val2) > 10 or (len(val1) + len(val2) >= 10)):
            raise LargeNumberException("Number too large for power.")
        operands.append(get_result(val1, val2, op))
    else:
        val2 = None
        val1 = operands.pop()
        op = operations.pop()
        operands.append(get_result(val1, val2, op))


def check_next_char(expression, i):
    while expression[i + 1] == ' ':
        assert expression[i + 1] == ' '
        assert len(expression) - i > 0
        i += 1
    assert expression[i+1] != ' '
    if expression[i + 1].isdigit() or expression[i + 1] == '(' or expression[i + 1] == ')' \
            or expression[i] in '+*-^' and expression[i + 1] == '√':
        return False
    return True


def check_close_parenthesis(operations):
    assert type(operations) == list
    if '(' in operations:
        return False
    return True


def check_parenthesis(operations):
    assert type(operations) == list
    if operations.count('(') == operations.count(')'):
        return False
    return True


def evaluate(expression):
    operands = []
    operations = []
    i = 0
    assert type(expression) == str
    assert len(expression) > 0
    while i < len(expression):
        assert len(expression) - i > 0
        if expression[i] == ' ':
            i += 1
            continue
        elif expression[i] == '(':
            operations.append(expression[i])
        elif expression[i].isdigit():
            val = ''
            assert expression[i]
            while i < len(expression) and expression[i].isdigit():
                val += expression[i]
                i += 1
            operands.append(val)
            i -= 1
        elif expression[i] == ')':
            if check_close_parenthesis(operations):
                raise InvalidExpressionException(
                    'The expression is INVALID. You can not close a parenthesis without to open one.')
            assert len(operations) > 0
            while len(operations) != 0 and operations[-1] != '(':
                compute_operation(operands, operations)
            operations.pop()
        else:
            try:
                if check_next_char(expression, i):
                    raise InvalidExpressionException(
                        'The expression is INVALID. You can not have successions of operators.')
            except Exception as e:
                raise InvalidExpressionException("The expression is INVALID. Operation without both or any operand.")
            while len(operations) != 0 and get_prio(operations[-1]) >= get_prio(expression[i]):
                compute_operation(operands, operations)
            operations.append(expression[i])
        i += 1
    while len(operations) != 0:
        if check_parenthesis(operations):
            raise InvalidExpressionException('The expression is INVALID. Check parenthesis.')
        compute_operation(operands, operations)
    return operands[-1]
