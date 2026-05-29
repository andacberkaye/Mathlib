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
-   Add trigonometric functions (sin, cos, tan)
-   Add logarithmic functions
-   Improve floating point precision handling
-   Add unit tests using pytest
-   Prepare PyPI release

## Notes

-   Division by zero raises errors
-   Some functions require at least one argument
-   Floating point precision may affect range-based operations
-   The project is not yet production-ready

## Status

Under active development

## Author

Python math utilities project focused on clean code and modular design.

---