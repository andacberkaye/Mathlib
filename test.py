from Core import transactions as ts

# -------------------------
# BASIC ARITHMETIC
# -------------------------

print("add(1, 2, 3, 4, 5) =", ts.add(1, 2, 3, 4, 5))
# Output: 15

print("sub(2, 3, 4, 5, -20) =", ts.sub(2, 3, 4, 5, -20))
# Output: 10

print("division(2, 3) =", ts.division(2, 3))
# Output: 0.666...

print("multi(5, 7, 8, 2, 9) =", ts.multi(5, 7, 8, 2, 9))
# Output: 5040

print("mod(20, 7) =", ts.mod(20, 7))
# Output: 6

print("power(2, 3) =", ts.power(2, 3))
# Output: 8

print("absolute(-6) =", ts.absolute(-6))
# Output: 6

# -------------------------
# MIN / MAX / AVG
# -------------------------

print("minimum(6, 7, 42, 4, 2) =", ts.minimum(6, 7, 42, 4, 2))
# Output: 2

print("maximum(6, 27, 43, 186, 67) =", ts.maximum(6, 27, 43, 186, 67))
# Output: 186

print("avg(2, 3, 4, 5, 60, 32, 7) =", ts.avg(2, 3, 4, 5, 60, 32, 7))
# Output: ~16

# -------------------------
# FACTORIAL / PRIME / PARITY
# -------------------------

print("factorial(5) =", ts.factorial(5))
# Output: 120

print("parity(83) =", ts.parity(83))
# Output: Odd

print("is_prime(13) =", ts.is_prime(13))
# Output: True

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

print("cube_root(27) =", ts.cube_root(27))        
# Output: 3.0

print("cube_root(64) =", ts.cube_root(64))        
# Output: 4.0

print("nth_root(16, 4) =", ts.nth_root(16, 4))    
# Output: 2.0

print("nth_root(81, 4) =", ts.nth_root(81, 4))    
# Output: 3.0

print("percentage(200, 15) =", ts.percentage(200, 15))
# Output: 30.0

print("percentage(50, 10) =", ts.percentage(50, 10))  
# Output: 5.0

# -------------------------
# ROUNDING FUNCTIONS
# -------------------------

print("round_number(3.6) =", ts.round_number(3.6))   
# Output: 4

print("round_number(3.4) =", ts.round_number(3.4))   
# Output: 3

print("round_number(-2.7) =", ts.round_number(-2.7)) 
# Output: -3

print("ceil_number(3.1) =", ts.ceil_number(3.1))     
# Output: 4

print("ceil_number(3.0) =", ts.ceil_number(3.0))     
# Output: 3

print("ceil_number(-3.1) =", ts.ceil_number(-3.1))   
# Output: -3

print("floor_number(3.9) =", ts.floor_number(3.9))   
# Output: 3

print("floor_number(3.0) =", ts.floor_number(3.0))   
# Output: 3

print("floor_number(-3.9) =", ts.floor_number(-3.9)) 
# Output: -4

# -------------------------
# TRIGONOMETRY FUNCTIONS (radians)
# -------------------------

print("sin(0) =", ts.sin(0))                     
# Output: 0 (approx)

print("sin(1.5708) =", ts.sin(1.5708))           
# Output: ~1 (pi/2) (approx)

print("cos(0) =", ts.cos(0))                     
# Output: 1 (approx)

print("cos(1.5708) =", ts.cos(1.5708))           
# Output: ~0 (approx)

print("tan(0) =", ts.tan(0))                     
# Output: 0 (approx)

print("tan(0.7854) =", ts.tan(0.7854))           
# Output: ~1 (pi/4) (approx)

print("cot(0.7854) =", ts.cot(0.7854))           
# Output: ~1 (approx)

print("cot(1.5708) =", ts.cot(1.5708))           
# Output: ~0 (very small) (approx)