from Core import transactions as ts

# -------------------------
# BASIC ARITHMETIC
# -------------------------

print("add(1, 2, 3, 4, 5) =", ts.add(1, 2, 3, 4, 5))
print("sub(2, 3, 4, 5, -20) =", ts.sub(2, 3, 4, 5, -20))
print("division(2, 3) =", ts.division(2, 3))
print("multi(5, 7, 8, 2, 9) =", ts.multi(5, 7, 8, 2, 9))
print("mod(20, 7) =", ts.mod(20, 7))
print("power(2, 3) =", ts.power(2, 3))
print("absolute(-6) =", ts.absolute(-6))

# -------------------------
# MIN / MAX / AVG
# -------------------------

print("minimum(6, 7, 42, 4, 2) =", ts.minimum(6, 7, 42, 4, 2))
print("maximum(6, 27, 43, 186, 67) =", ts.maximum(6, 27, 43, 186, 67))
print("avg(2, 3, 4, 5, 60, 32, 7) =", ts.avg(2, 3, 4, 5, 60, 32, 7))

# -------------------------
# FACTORIAL / PRIME / PARITY
# -------------------------

print("factorial(5) =", ts.factorial(5))
print("parity(83) =", ts.parity(83))
print("is_prime(13) =", ts.is_prime(13))

# -------------------------
# GCD / LCM
# -------------------------

print("gcd(60, 36) =", ts.gcd(60, 36))
# Output: 12

print("lcm(12, 18) =", ts.lcm(12, 18))
# Output: 36

# -------------------------
# PRIME FACTORS
# -------------------------

print("prime_factors(84) =", ts.prime_factors(84))
# Output: [2, 2, 3, 7]

# -------------------------
# FIBONACCI
# -------------------------

print("fibonacci(6, 'series') =", ts.fibonacci(6, "series"))
# Output: [0, 1, 1, 2, 3, 5]

print("fibonacci(6, 'number') =", ts.fibonacci(6, "number"))
# Output: 8

# -------------------------
# RANGE FUNCTIONS
# -------------------------

print("add_range(1, 5) =", ts.add_range(1, 5))
# Output: 15

print("add_range(1, 5, 2) =", ts.add_range(1, 5, 2))
# Output: 9

# -------------------------
# ROOT FUNCTIONS
# -------------------------

print("sqrt(16) =", ts.sqrt(16))
# Output: 4.0