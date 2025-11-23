import math
## Application Code

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def sqrt(a):
    if a < 0:
        return None
    return math.sqrt(a)

def power(a, b):
    return a ** b

def factorial(n):
    if n < 0:
        return None
    return math.factorial(n)  

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def absolute(a):
    return abs(a)
