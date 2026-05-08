'''
Q.2) Write a Python program for the following Cryptarithmetic problems. GO + TO = OUT
[20 Marks]
'''

from itertools import permutations

def solve_cryptarithmetic():
    # GO + TO = OUT
    letters = set('GTOU')
    
    for perm in permutations(range(10), len(letters)):
        sol = dict(zip(letters, perm))
        
        if sol['G'] == 0 or sol['T'] == 0 or sol['O'] == 0:
            continue
            
        GO = sol['G']*10 + sol['O']
        TO = sol['T']*10 + sol['O']
        OUT = sol['O']*100 + sol['U']*10 + sol['T']
        
        if GO + TO == OUT:
            print(f"Solution found:")
            print(f"  G={sol['G']}, O={sol['O']}, T={sol['T']}, U={sol['U']}")
            print(f"  {GO} + {TO} = {OUT}")
            return
    
    print("No solution found")

solve_cryptarithmetic()
