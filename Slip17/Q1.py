'''
Q.1) Python program that demonstrates the hill climbing algorithm to find the maximum of a mathematical function.
[10 Marks]
'''

import random

def hill_climbing(func, start, step_size=0.1, max_iter=1000):
    current = start
    for i in range(max_iter):
        current_val = func(current)
        next_val1 = func(current + step_size)
        next_val2 = func(current - step_size)
        
        if next_val1 > current_val:
            current += step_size
        elif next_val2 > current_val:
            current -= step_size
        else:
            break
            
    return current, func(current)

# Define the function f(x) = -x^2 + 4x
def f(x):
    return -x**2 + 4*x

# Find maximum
max_x, max_val = hill_climbing(f, 0)
print(f"Maximum at x = {max_x:.2f}, f(x) = {max_val:.2f}")
