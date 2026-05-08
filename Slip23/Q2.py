'''
Q.2) Write a Python program for the following Cryptarithmetic problems CROSS+ROADS = DANGER
[20 Marks]
'''

from itertools import permutations

def solve_cryptarithmetic():
    # CROSS + ROADS = DANGER
    letters = set('CROSSROADNGER')
    unique_letters = set('CROSADNGER')  # Remove duplicates
    
    for perm in permutations(range(10), len(unique_letters)):
        sol = dict(zip(unique_letters, perm))
        
        if sol['C'] == 0 or sol['R'] == 0 or sol['D'] == 0:
            continue
            
        # Handle duplicate letters
        CROSS = sol['C']*10000 + sol['R']*1000 + sol['O']*100 + sol['S']*10 + sol['S']
        ROADS = sol['R']*10000 + sol['O']*1000 + sol['A']*100 + sol['D']*10 + sol['S']
        DANGER = sol['D']*100000 + sol['A']*10000 + sol['N']*1000 + sol['G']*100 + sol['E']*10 + sol['R']
        
        if CROSS + ROADS == DANGER:
            print(f"Solution found:")
            print(f"  C={sol['C']}, R={sol['R']}, O={sol['O']}, S={sol['S']}")
            print(f"  A={sol['A']}, D={sol['D']}, N={sol['N']}, G={sol['G']}, E={sol['E']}")
            print(f"  {CROSS} + {ROADS} = {DANGER}")
            return
    
    print("No solution found")

solve_cryptarithmetic()
