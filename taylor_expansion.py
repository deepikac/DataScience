import sympy as sy
import numpy as np

# Define the variable and the function to approximate
x = sy.Symbol('x')

# Factorial function
def factorial(n):
    return np.math.factorial(n)


# Taylor approximation at x0 of the function 'function'
def taylor(function, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i += 1
    return p

