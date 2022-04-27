import math 

def get_prio(operand):     
    if operand == '+' or operand == '-':
        return 1
    if operand == '*' or operand == '/':
        return 2
    if operand == '√' or operand == '^':
        return 3
    return 0

def get_result(a, b, operand):
    if operand == '+': return eval(f'{a} + {b}')
    if operand == '-': return eval(f'{a} - {b}')
    if operand == '*': return eval(f'{a} * {b}')
    if operand == '/': return eval(f'{a} // {b}')
    if operand == '^': return eval(f'{a} ** {b}')
    if operand == '√': return math.sqrt(int(a))

def compute_operation(operands, operations):
  if operations[-1] != '√':         
      val2 = operands.pop()
      val1 = operands.pop()
      op = operations.pop()
      operands.append(get_result(val1, val2, op))
  else:
      val2 = None
      val1 = operands.pop()
      op = operations.pop()
      operands.append(get_result(val1, val2, op))

def check_next_char(expression, i):
  while expression[i+1] == ' ':
      i += 1
  if expression[i+1].isdigit() or expression[i+1] == '(' or expression[i+1] == ')':
    return False
  return True

def check_close_paranthesis(operations):
  if '(' in operations:
    return False
  return True

def check_paranthesis(operations):
  if operations.count('(') == operations.count(')'):
    return False
  return True
  
def evaluate(expression):
     
    operands = []
    operations = []
    i = 0
    
    try:
      while i < len(expression):
          
          if expression[i] == ' ':
              i += 1
              continue
          
          elif expression[i] == '(':
              operations.append(expression[i])
          
          elif expression[i].isdigit():
              val = ''
              while i < len(expression) and expression[i].isdigit():
                  val += expression[i]
                  i += 1
              operands.append(val)
              i-=1

          elif expression[i] == ')':
              if check_close_paranthesis(operations):
                raise Exception('The expression is INVALID. You can not close a parenthesis without to open one.')
              while len(operations) != 0 and operations[-1] != '(':
                  compute_operation(operands, operations)
              operations.pop()
          
          else:
              if check_next_char(expression, i):
                raise Exception('The expression is INVALID. You can not have successions of operators.')
              while len(operations) != 0 and get_prio(operations[-1]) >= get_prio(expression[i]):
                  compute_operation(operands, operations)
              operations.append(expression[i])
          i += 1

      while len(operations) != 0:
          if(check_paranthesis(operations)):
            raise Exception('The expression is INVALID. Check parenthesis.')
          compute_operation(operands, operations)

      return operands[-1]
    except Exception as e:
      print(e)

print(evaluate("√(4+5)^(2 * 2) - 2 + 10 + 2 * 6"))
print(evaluate("1000 * ( 2 + 12 ) / 14 + (( 2 + 5 ) * (3 - 3))"))