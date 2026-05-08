'''
Q.1) Write a python program using mean end analysis algorithm problem of transforming a string of lowercase letters into another string.
[10 Marks]
'''

def mean_end_analysis(start, goal):
    print(f"Transforming '{start}' to '{goal}' using Mean-End Analysis")
    
    current = list(start)
    target = list(goal)
    steps = []
    
    for i in range(len(current)):
        if i < len(target) and current[i] != target[i]:
            steps.append(f"Change position {i+1} from '{current[i]}' to '{target[i]}'")
            current[i] = target[i]
    
    print("Steps:")
    for step in steps:
        print(f"- {step}")
    
    print(f"Final result: {''.join(current)}")

# Example usage
start_str = "abc"
goal_str = "xyz"
mean_end_analysis(start_str, goal_str)
