'''
Q.2) Write a Python program to solve water jug problem. Two jugs with capacity 4 gallon and 3 gallon are given with unlimited water supply respectively. The target is to achieve 2 gallon of water in second jug.
[20 Marks]
'''

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    visited = set()
    stack = [(0, 0, [])]  # (jug1, jug2, path)
    
    while stack:
        jug1, jug2, path = stack.pop()
        
        if (jug1, jug2) in visited:
            continue
            
        visited.add((jug1, jug2))
        current_path = path + [(jug1, jug2)]
        
        print(f"Jug1: {jug1}, Jug2: {jug2}")
        
        if jug2 == target:
            print("Target achieved!")
            print("Path to solution:")
            for step in current_path:
                print(f"  {step}")
            return
        
        # Generate next states
        next_states = []
        
        # Fill jug1
        next_states.append((jug1_capacity, jug2))
        # Fill jug2
        next_states.append((jug1, jug2_capacity))
        # Empty jug1
        next_states.append((0, jug2))
        # Empty jug2
        next_states.append((jug1, 0))
        # Pour jug1 to jug2
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        next_states.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        # Pour jug2 to jug1
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        next_states.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))
        
        for state in next_states:
            if state not in visited:
                stack.append((state[0], state[1], current_path))
    
    print("No solution found")

print("Water Jug Problem (4-gallon and 3-gallon jugs, target 2 gallons):")
water_jug_problem(4, 3, 2)
