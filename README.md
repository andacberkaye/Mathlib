# MathLib

A lightweight Python math utility library providing basic arithmetic, number theory, sequence operations, and mathematical helper functions.

> This project is under active development and is not yet stable for production use. The library is planned to grow to 50+ functions before being published on PyPI.

---

## Features

### Basic Operations
- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Power
- Absolute value
- Rounding (round, ceil, floor)

### Statistics & Utilities
- Minimum / Maximum
- Average
- Percentage calculations
- Percentage change

### Number Theory
- GCD (Greatest Common Divisor)
- LCM (Least Common Multiple)
- Prime check
- Prime factorization
- Parity (Even / Odd)

### Sequences
- Fibonacci (number / series)
- Range-based sum
- Range-based product

### Mathematical Functions
- Factorial
- Square root
- Cube root
- Nth root
- Trigonometric functions (sin, cos, tan, cot)
- Hypotenuse calculation

### Advanced Mathematics
- Taylor series based trigonometric calculations
- Newton method square root approximation
- Floating point safe calculations

---

## Installation

Clone the repository:

```bash
git https://github.com/andacberkaye/MathLib
cd MathLib
```
---

## Import

Import the module

```python
    from Core import transactions
```

## Usage Examples

### Advanced Math Functions

```python
ts.round_number(3.6)
ts.ceil_number(3.1)
ts.floor_number(3.9)

ts.cube_root(27)
ts.nth_root(16, 4)

ts.percentage(200, 15)

ts.sin(0)
ts.cos(1.5708)
ts.tan(0.7854)
ts.cot(0.7854)

ts.hypotenuse(3, 4)
```

### Basic Operations

```python
    ts.add(1, 2, 3)
    ts.sub(10, 3, 2)
    ts.multi(2, 3, 4)
    ts.division(10, 2)
```

### Number Theory

```python
    ts.gcd(60, 36)
    ts.lcm(12, 18)
    ts.prime_factors(84)
    ts.is_prime(13)
```

### Fibonacci

```python
    ts.fibonacci(6, "series")
    ts.fibonacci(6, "number")   
```

### Range Operations

```python
    ts.add_range(1, 5)
    ts.product_range(1, 5)
```

### Square Roots

```python
    ts.sqrt(16)
```

### Basic Operations

```python
    from Core import transactions
```

## Roadmap

-   Expand to 50+ functions
-   Add full trigonometric system (sin, cos, tan, cot)
-   Add root functions (cube root, nth root)
-   Improve numerical accuracy and convergence control
-   Add logarithmic functions
-   Improve floating point precision handling
-   Add unit tests using pytest
-   Prepare PyPI release

## Notes

-   Division by zero raises errors
-   Some functions require at least one argument
-   Floating point precision may affect range-based operations
-   The project is not yet production-ready
-   Trigonometric functions use Taylor series approximation
-   Results may slightly differ from Python's math module due to floating point precision

## Status

Under active development

## Author

Python math utilities project focused on clean code and modular design.

---