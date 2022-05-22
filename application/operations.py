from application.exceptions import DivisionByZeroException, NegativeNumberException


def summation(a, b):
    assert len(a) > 0
    assert len(b) > 0
    if len(a) < len(b):
        a, b = b[::-1], a[::-1]
    else:
        a, b = a[::-1], b[::-1]
    result = ''
    carry = 0
    index = 0
    while index < len(b):
        assert len(b) - index > 0
        digit = int(b[index]) + int(a[index])
        result += str((digit + carry) % 10) if digit + carry > 9 else str(digit + carry)
        carry = 1 if digit + carry > 9 else 0
        index += 1
    assert index == len(b)
    while index < len(a):
        assert len(a) - index > 0
        digit = int(a[index])
        result += str((digit + carry) % 10) if digit + carry > 9 else str(digit + carry)
        carry = 1 if digit + carry > 9 else 0
        index += 1
    assert len(a) == index
    assert len(result) > 0
    return (result + ('1' if carry > 0 else ''))[::-1]


def multiplication(a, b):
    if b == '0' or a == '0':
        return '0'
    times = '1'
    result = a
    while times != b:
        assert is_smaller(times, b)
        result = summation(result, a)
        times = summation(times, '1')
    assert times == b
    return result


def power(base, exponent):
    assert len(exponent) > 0
    assert len(base) > 0
    if base == '0':
        return '0'
    elif base == '1':
        return '1'
    elif exponent == '0':
        return '1'
    elif exponent == '1':
        return base
    times = '1'
    result = base
    while times != exponent:
        assert is_smaller(times, exponent)
        result = multiplication(result, base)
        times = summation(times, '1')
    assert times == exponent
    return result


def is_smaller(str1, str2):
    assert len(str1) > 0
    assert len(str2) > 0
    n1 = len(str1)
    n2 = len(str2)
    if n1 < n2:
        return True
    if n2 < n1:
        return False
    for i in range(n1):
        if str1[i] < str2[i]:
            return True
        elif str1[i] > str2[i]:
            return False
    return False


def subtraction(str1, str2):
    assert len(str1) > 0
    assert len(str2) > 0
    if str1 == '0':
        return '-' + str2
    if is_smaller(str1, str2):
        temp = str1
        str1 = str2
        str2 = temp
    result = ""
    n1 = len(str1)
    n2 = len(str2)
    str1 = str1[::-1]
    str2 = str2[::-1]
    carry = 0
    for i in range(n2):
        sub = ((ord(str1[i]) - ord('0')) - (ord(str2[i]) - ord('0')) - carry)
        if sub < 0:
            sub = sub + 10
            carry = 1
        else:
            carry = 0
        result = result + str(sub)
    for i in range(n2, n1):
        sub = ((ord(str1[i]) - ord('0')) - carry)
        if sub < 0:
            sub = sub + 10
            carry = 1
        else:
            carry = 0
        result = result + str(sub)
    result = result[::-1]
    if result[0] == '0':
        result = result[1:]
    return '0' if result == '' else result


def division(a, b):
    assert len(a) > 0
    assert len(b) > 0
    result = '0'
    if b == '0':
        raise DivisionByZeroException("Division by 0.")
    if a == '0':
        return '0'
    while is_smaller(b, a) or a == b:
        assert len(subtraction(a, b)) > 0
        a = subtraction(a, b)
        result = summation(result, '1')
    return result


def square_root(number):
    if number == '0' or number == '1':
        return number
    if '-' in number:
        raise NegativeNumberException("Negative number.")
    result = '1'
    temporary_power = multiplication(result, result)
    while is_smaller(temporary_power, number):
        assert len(subtraction(number, temporary_power)) > 0
        result = summation(result, '1')
        temporary_power = multiplication(result, result)
    if temporary_power != number and is_smaller('1', temporary_power):
        result = subtraction(result, '1')
    return result
