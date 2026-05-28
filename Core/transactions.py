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
    
    else:
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
    else: 
        return p / b
    
