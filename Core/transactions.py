def add(*args):
    """
    Adds the entered numbers.

    Parameters:
        *args (int | float):
            Any number of integer or float values.

    Returns:
        int | float:
            Sum of all entered numbers.
    """

    addition = 0

    for i in args:
        addition += i
    
    return addition
