'''
Q.2) Write a Python program for the following Cryptarithmetic problems SEND + MORE = MONEY
[20 Marks]
'''

from itertools import permutations

def solve_cryptarithmetic():
    # SEND + MORE = MONEY
    letters = set('SENDMORY')
    
    for perm in permutations(range(10), len(letters)):
        sol = dict(zip(letters, perm))
        
        if sol['S'] == 0 or sol['M'] == 0:
            continue
            
        SEND = sol['S']*1000 + sol['E']*100 + sol['N']*10 + sol['D']
        MORE = sol['M']*1000 + sol['O']*100 + sol['R']*10 + sol['E']
        MONEY = sol['M']*10000 + sol['O']*1000 + sol['N']*100 + sol['E']*10 + sol['Y']
        
        if SEND + MORE == MONEY:
            print(f"Solution found:")
            print(f"  S={sol['S']}, E={sol['E']}, N={sol['N']}, D={sol['D']}")
            print(f"  M={sol['M']}, O={sol['O']}, R={sol['R']}, Y={sol['Y']}")
            print(f"  {SEND} + {MORE} = {MONEY}")
            return
    
    print("No solution found")

solve_cryptarithmetic()
