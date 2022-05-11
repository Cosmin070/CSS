# define Python user-defined exceptions
class LargeNumberException(Exception):
    """Raised for numbers too big"""
    pass

class InvalidExpressionException(Exception):
    """Raised for invalid expressions"""
    pass

class TagException(Exception):
    """Raised when there is a misplaced or misused tags"""
    pass

class DivisionByZeroException(Exception):
    """Raised when there is a division by zero"""
    pass

class NegativeNumberException(Exception):
    """Raised when there is a negative number"""
    pass

class NonXMLFileTypeException(Exception):
    """Raised when the uploaded file is not a .xml file"""
    pass