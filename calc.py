def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        ### For Unit testing the diviosn with non intger reminder ie with decimal###
        #raise ValueError('Can not divide by zero!')#
    #return x //#
         raise ValueError('Can not divide by zero!')
    return x / y

