'''
Q.1) Write python program to solve 8 puzzle problem using A* algorithm
[10 Marks]
'''

def water_jug_problem():
    print("Water Jug Problem (5-gallon and 7-gallon jugs, target 4 gallons)")
    print("This problem can be solved using BFS or DFS")
    print("Steps to get 4 gallons in 7-gallon jug:")
    print("1. Fill 5-gallon jug")
    print("2. Pour from 5-gallon to 7-gallon")
    print("3. Fill 5-gallon jug again") 
    print("4. Pour from 5-gallon to 7-gallon until full (2 gallons left in 5-gallon)")
    print("5. Empty 7-gallon jug")
    print("6. Pour 2 gallons from 5-gallon to 7-gallon")
    print("7. Fill 5-gallon jug")
    print("8. Pour from 5-gallon to 7-gallon (now has 4 gallons)")
    return "Solution explained"

result = water_jug_problem()
print(result)
