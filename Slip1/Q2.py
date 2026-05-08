'''
Q.2) Write a Python program to implement Depth First Search algorithm. Refer the following graph as an Input for the program. [Initial node=1,Goal node=8]
[20 Marks]
'''

def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start)
    path.append(start)
    
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path.copy())
            if result:
                return result
    return None

# Graph from slip 1 (Initial node=1, Goal node=8)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [8],
    6: [8],
    7: [8],
    8: []
}

print("DFS Path from 1 to 8:")
path = dfs(graph, 1, 8)
print(" -> ".join(map(str, path)) if path else "No path found")
