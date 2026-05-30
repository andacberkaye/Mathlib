def add(*args: float) -> float:
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

def sub(*args: float) -> float:
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

def division(p: float, b: float) -> float:
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
    
def multi(*args: float) -> float:
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

def mod(a: float, n: float) -> float:
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

def power(b: float,x: float) -> float:
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

    return b**x

def absolute(x: float) -> float:
    """
        Calculates the absolute value of the entered number

        Parameters:
            x (int | float):
                The number whose absolute value is calculated

        Return value:
            int | float:
                The number whose absolute value is calculated
    """

    if x < 0:
        return -x
    else:
        return x
    
def minimum(*args: float) -> float:
    """
        Finds the smallest of the entered numbers

        Parameters:
            args (int | float):
                The numbers entered, from which the smallest is to be found

        Return value:
            int | float:
                The smallest number found
    """
    if len(args) == 0:
        raise ValueError("At least one number is required")
    min_number = args[0]

    for i in args[1:]:
        if i < min_number:
            min_number = i
        else:
            continue
    return min_number

def maximum(*args: float) -> float:
    """
        Finds the biggest of the entered numbers

        Parameters:
            args (int | float):
                The numbers entered, from which the biggest is to be found

        Return value:
            int | float:
                The biggest number found
    """
    if len(args) == 0:
        raise ValueError("At least one number is required") 
    max_number = args[0]

    for i in args[1:]:
        if i > max_number:
            max_number = i
        else:
            continue
    return max_number

def avg(*args: float) -> float:
    """
        Calculates the average of the entered numbers

        Parameters:
            args (int | float):
                Calculates the average of the entered numbers

        Return value:
            int | float:
                The calculated average
    """
    if len(args) == 0:
        raise ValueError("At least one number is required")

    addition = 0

    for i in args:
        addition += i

    return addition / len(args)

def factorial(n: int) -> int:
    """
        Calculates the factorial of the entered number

        Parameters:
            n (int | float):
                Calculates the factorial of the entered number

        Return value:
            int | float:
                The number obtained as the factorial
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    fac = 1
    while n > 0:
        fac = fac*n
        n -= 1
    return fac

def parity(x: int) -> str:
    """
        Determines whether the entered number is even or odd

        Parameters:
            x (int | float):
                The number whose parity is to be determined

        Return value:
            int | float:
                The result of the parity calculation
    """

    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
def is_prime(x: int) -> bool:

    """
        Determines whether the entered number is prime

        Parameters:
            x (int | float):
                The number to be checked for primality

        Return value:
            int | float:
                The result of the primality check
    """

    if x <= 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True

def gcd(a: int, b: int) -> int:
    """
        Returns the greatest common divisor (GCD) of two integers.

        Parameters:
            a (int):
                First integer.

            b (int):
                Second integer.

        Return value:
            int:
                Greatest common divisor of the given integers.
    """

    while b != 0:
        a, b = b, a % b

    return absolute(a)

def lcm(a: int, b: int) -> int:
    """
    Returns the least common multiple (LCM) of two integers.

    Parameters:
        a (int):
            First integer.

        b (int):
            Second integer.

    Return value:
        int:
            Least common multiple of the given integers.
    """

    return absolute(a * b) // gcd(a, b)

def prime_factors(a: int) -> list[int]:
    """
        Returns the prime factors of a given integer.

        Parameters:
            number (int):
                Integer to factorize.

        Return value:
            list:
                List containing prime factors.
    """

    if a <= 1:
        raise ValueError("Number must be greater than 1")
    factors=[]
    divisor = 2

    while a > 1:
        while a % divisor == 0:
            factors.append(divisor)
            a //= divisor
        divisor += 1

    return factors

def fibonacci(n: int, mode: str) -> int | list[int]:
    """
    Fibonacci number or series generator.

    Parameters:
        n (int):
            Number of elements (for series) or position (for number mode)

        mode (str):
            "series" -> returns fibonacci series
            "number" -> returns nth fibonacci number

    Return value:
        int | list[int]:
            Fibonacci number or fibonacci sequence
    """

    if n < 0:
        raise ValueError("n must be >= 0")

    a, b = 0, 1

    if mode == "number":
        for _ in range(n):
            a, b = b, a + b
        return a

    elif mode == "series":
        series = []

        for _ in range(n):
            series.append(a)
            a, b = b, a + b

        return series

    else:
        raise ValueError("mode must be 'series' or 'number'")
    
def add_range(start: float, end: float, amount: float = 1) -> float:
    """
    Calculates the sum of numbers in a given range with a step value.

    The function starts from 'start' and adds numbers up to 'end'
    by increasing each step with 'amount'. If 'amount' is not provided,
    it defaults to 1.

    Parameters:
        start (float):
            The starting value of the range.

        end (float):
            The ending value of the range (inclusive).

        amount (float, optional):
            The step size between numbers. Default is 1.
            Must not be 0.

    Returns:
        float:
            The sum of all numbers in the range.

    Raises:
        ValueError:
            If amount is 0.
    """

    if amount == 0:
        raise ValueError("amount cannot be 0")

    total = 0
    current = start

    while current <= end:
        total += current
        current += amount

    return total

def sqrt(a: float) -> float:
    """
    Calculates the square root of a number.

    The function returns the value which, when multiplied by itself,
    gives the original number (a).

    Parameters:
        a (float):
            The number to calculate the square root of.
            Must be >= 0 for real results.

    Returns:
        float:
            The square root of the given number.

    Raises:
        ValueError:
            If a is negative (since real square root is undefined).
    """

    if a < 0:
        raise ValueError("Square root of negative number is not real")
    return a ** 0.5

def cube_root(x: float) -> float:
    """
    Calculates the cube root of a number.

    The function returns the value which, when multiplied by itself
    three times, gives the original number.

    Parameters:
        x (float):
            The number whose cube root is to be calculated.

    Returns:
        float:
            The cube root of the given number.
    """

    return absolute(x) ** (1 / 3)

def nth_root(x: float, n: int) -> float:
    """
    Calculates the nth root of a number.

    The function returns the value which, when raised to the power
    of n, gives the original number.

    Parameters:
        x (float):
            The number whose root is to be calculated.

        n (int):
            The degree of the root.

    Returns:
        float:
            The nth root of the given number.

    Raises:
        ValueError:
            If n is 0.
            If x is negative and n is even.
    """

    if n == 0:
        raise ValueError("n cannot be 0")

    if x < 0 and n % 2 == 0:
        raise ValueError("Even root of a negative number is not real")

    if x >= 0:
        return x ** (1 / n)
    else:
        return -((-x) ** (1 / n))
    
def percentage(value: float, percent: float) -> float:
    """
    Calculates a percentage of a given value.

    Parameters:
        value (float):
            The original value.

        percent (float):
            The percentage to calculate.

    Returns:
        float:
            The calculated percentage of the value.
    """

    return value * percent / 100

def round_number(x: float) -> int:
    """
    Rounds a number to the nearest integer.

    Parameters:
        x (float):
            The number to be rounded.

    Returns:
        int:
            The nearest integer to the given number.
    """
    if x >= 0:
        return int(x + 0.5)
    else:
        return int(x - 0.5)

def ceil_number(x: float) -> int:
    """
    Returns the smallest integer greater than or equal to x.

    Parameters:
        x (float):
            The number to be rounded up.

    Returns:
        int:
            The smallest integer greater than or equal to x.
    """
    if x == int(x):
        return int(x)
    return int(x) + (1 if x > 0 else 0)

def floor_number(x: float) -> int:
    """
    Returns the greatest integer less than or equal to x.

    Parameters:
        x (float):
            The number to be rounded down.

    Returns:
        int:
            The greatest integer less than or equal to x.
    """
    if x == int(x):
        return int(x)
    return int(x) - (1 if x < 0 else 0)

import math


def sin(x: float) -> float:
    """
    Calculates sine using Taylor series approximation.

    Parameters:
        x (float):
            Angle in radians.

    Returns:
        float:
            Approximate sine value.
    """
    result = 0.0
    term = x

    for i in range(10):
        result += term
        term *= -x * x / ((2 * i + 2) * (2 * i + 3))

    return result


def cos(x: float) -> float:
    """
    Calculates cosine using Taylor series approximation.

    Parameters:
        x (float):
            Angle in radians.

    Returns:
        float:
            Approximate cosine value.
    """
    result = 1.0
    term = 1.0

    for i in range(1, 10):
        term *= -x * x / ((2 * i - 1) * (2 * i))
        result += term

    return result


def tan(x: float) -> float:
    """
    Calculates tangent as sin(x) / cos(x).

    Parameters:
        x (float):
            Angle in radians.

    Returns:
        float:
            Approximate tangent value.
    """
    c = cos(x)
    if abs(c) < 1e-12:
        raise ValueError("tan undefined (cos(x) too close to 0)")
    return sin(x) / c


def cot(x: float) -> float:
    """
    Calculates cotangent as cos(x) / sin(x).

    Parameters:
        x (float):
            Angle in radians.

    Returns:
        float:
            Approximate cotangent value.
    """
    s = sin(x)
    if abs(s) < 1e-12:
        raise ValueError("cot undefined (sin(x) too close to 0)")
    return cos(x) / s


def hypotenuse(a: float, b: float) -> float:
    """
    Calculates hypotenuse using Newton's method (no math.sqrt).

    Parameters:
        a (float):
            First side.

        b (float):
            Second side.

    Returns:
        float:
            Hypotenuse value.
    """
    value = a * a + b * b

    result = value
    for _ in range(10):
        result = (result + value / result) / 2

    return result

