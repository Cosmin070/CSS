# define Python user-defined exceptions
class large_number_exception(Exception):
    """Raised for numbers too big"""
    pass

class invalid_expression_exception(Exception):
    """Raised for invalid expressions"""
    pass

class tag_exception(Exception):
    """Raised when there is a misplaced or misused tags"""
    pass

class division_by_zero_exception(Exception):
    """Raised when there is a division by zero"""
    pass

class negative_number_exception(Exception):
    """Raised when there is a negative number"""
    pass