def summation(a, b):
    if len(a) < len(b):
        a, b = b[::-1], a[::-1]
    else:
        a, b = a[::-1], b[::-1]
    result = ''
    carry = 0
    index = 0
    while index < len(b):
        digit = int(b[index]) + int(a[index])
        result += str((digit + carry) % 10) if digit + carry > 9 else str(digit + carry)
        carry = 1 if digit + carry > 9 else 0
        index += 1
    while index < len(a):
        digit = int(a[index])
        result += str((digit + carry) % 10) if digit + carry > 9 else str(digit + carry)
        carry = 1 if digit + carry > 9 else 0
        index += 1
    return (result + ('1' if carry > 0 else ''))[::-1]


def multiplication(a, b):
    if b == '0' or a == '0':
        return '0'
    times = '1'
    result = a
    while times != b:
        result = summation(result, a)
        times = summation(times, '1')
    return result


def power(base, exponent):
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
        result = multiplication(result, base)
        times = summation(times, '1')
    return result


def is_smaller(str1, str2):
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
    return result


def division(a, b):
    result = ''
    if b == '0':
        raise Exception("Division by 0.")
    if a == '0':
        return '0'
    while is_smaller(b, a) or a == b:
        a = subtraction(a, b)
        result = summation(result, '1')
    return result


def square_root(number):
    if number == '0' or number == '1':
        return number
    if '-' in number:
        raise Exception("Negative number.")
    result = '1'
    temporary_power = multiplication(result, result)
    while is_smaller(temporary_power, number):
        result = summation(result, '1')
        temporary_power = multiplication(result, result)
    if temporary_power != number and is_smaller('1', temporary_power):
        result = subtraction(result, '1')
    return result
