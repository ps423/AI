'''
Q.1) Write Python program to implement crypt arithmetic problem TWO+TWO=FOUR
[10 Marks]
'''

from itertools import permutations

def solve_cryptarithmetic():
    # TWO + TWO = FOUR
    letters = set('TWOFUR')
    
    for perm in permutations(range(10), len(letters)):
        sol = dict(zip(letters, perm))
        
        if sol['T'] == 0 or sol['F'] == 0:
            continue
            
        TWO = sol['T']*100 + sol['W']*10 + sol['O']
        FOUR = sol['F']*1000 + sol['O']*100 + sol['U']*10 + sol['R']
        
        if TWO + TWO == FOUR:
            print(f"Solution found:")
            print(f"  T={sol['T']}, W={sol['W']}, O={sol['O']}")
            print(f"  F={sol['F']}, U={sol['U']}, R={sol['R']}")
            print(f"  {TWO} + {TWO} = {FOUR}")
            return
    
    print("No solution found")

solve_cryptarithmetic()
