def add(*args):
    """
    Adds the entered numbers in order.

    Parameters:
        *args (int | float):
            Any number of integer or float values.

    Return value:
        int | float:
            The sum of all entered numbers.
    """

    addition = 0

    for i in args:
        addition += i
    
    return addition

def sub(*args):
    """
        Subtracts the entered numbers in order.

        Parameters:
            - At least one number is required

            *args (int | float):
                Any number of integer or float values.

        Return value:
            int | float:
                The subtracting all entered numbers.
    """

    if len(args) == 0:
        raise ValueError("At least one number is required")
    subtract = args[0]

    for i in args[1:]:
        subtract -= i
    
    return subtract

def division(p, b):
    """
        Divides two numbers.

        Parameters:
            p (int | float):
                Dividend number

            b (int | float):
                Divisor number

        Returns:
            int | float:
                Division result
    """
        
    if b == 0:
        raise ZeroDivisionError("A divisor cannot be zero")
    return p / b
    
def multi(*args):
    """
        Multiplication the entered numbers in order.

        Parameters:
            *args (int | float):
                Any number of integer or float values.

        Return value:
            int | float:
                The multiplication of all entered numbers.
    """

    if len(args) == 0:
        raise ValueError("At least one number is required")
    
    multiplication = args[0]

    for i in args[1:]:
        multiplication *= i
    
    return multiplication

def mod(a, n):
    """
        Calculates the modulus of the first number relative to the second.

        Parameters:
            a (int | float):
                The number for which the modulus is calculated

            n (int | float):
                The divisor

        Return value:
            int | float:
                The result of the modulus operation
    """
    
    if n == 0:
        raise ZeroDivisionError("A divisor cannot be zero")
    return a % n

def power(b,x):
    """
    Calculates the power of the first number raised to the second number

        Parameters:
            b (int | float):
                The number to be raised to a power

            x (int | float):
                The exponent

        Return value:
            int | float:
                The result of raising the first number to the second number
    """

    return b^x


