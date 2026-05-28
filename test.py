from Core import transactions as ts

# Addition
print("add(1, 2, 3, 4, 5) =", ts.add(1, 2, 3, 4, 5))
# Output: 15

# Subtraction (left to right)
print("sub(2, 3, 4, 5, -20) =", ts.sub(2, 3, 4, 5, -20))
# Output: 10
# Explanation: 2 - 3 - 4 - 5 - (-20) = 10

# Division
print("division(2, 3) =", ts.division(2, 3))
# Output: 0.6666666666666666

# Multiplication
print("multi(5, 7, 8, 2, 9) =", ts.multi(5, 7, 8, 2, 9))
# Output: 5040

# Modulus
print("mod(20, 7) =", ts.mod(20, 7))
# Output: 6

# Power
print("power(2, 3) =", ts.power(2, 3))
# Output: 8

# Absolute value
print("absolute(-6) =", ts.absolute(-6))
# Output: 6

# Minimum value
print("minumum(6, 7, 42, 4, 2) =", ts.minumum(6, 7, 42, 4, 2))
# Output: 2

# Maximum value
print("maximum(6, 27, 43, 186, 67) =", ts.maximum(6, 27, 43, 186, 67))
# Output: 186

# Average
print("avg(2, 3, 4, 5, 60, 32, 7) =", ts.avg(2, 3, 4, 5, 60, 32, 7))
# Output: 16.142857142857142

# Factorial
print("factorial(5) =", ts.factorial(5))
# Output: 120

# Parity check
print("parity(83) =", ts.parity(83))
# Output: Odd

# Prime check
print("is_prime(13) =", ts.is_prime(13))
# Output: True