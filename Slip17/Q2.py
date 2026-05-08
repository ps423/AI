'''
Q.2) Write a Python program to implement A* algorithm. Refer the following graph as an Input for the program.[ Start vertex is A and Goal Vertex is G]
[20 Marks]
'''

import heapq

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], 0, start, [start]))
    visited = set()
    
    while open_set:
        f_cost, g_cost, current, path = heapq.heappop(open_set)
        
        if current in visited:
            continue
            
        visited.add(current)
        
        if current == goal:
            return path, g_cost
        
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g_cost = g_cost + cost
                new_f_cost = new_g_cost + heuristic[neighbor]
                heapq.heappush(open_set, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))
    
    return None, float('inf')

# Example graph (Start: A, Goal: G)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1), ('G', 3)],
    'D': [('G', 8)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values (straight-line distance to G)
heuristic = {
    'A': 7, 'B': 6, 'C': 2, 'D': 5, 'E': 1, 'F': 1, 'G': 0
}

print("A* Algorithm from A to G:")
path, cost = a_star(graph, 'A', 'G', heuristic)
if path:
    print(f"Path: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print("No path found")
