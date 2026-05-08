'''
Q.2) Write a Python program to implement Breadth First Search algorithm. Refer the following graph as an Input for the program.[Initial node=1,Goal node=8]
[20 Marks]
'''

from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
            
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None

# Graph for slip 5 (Initial node=1, Goal node=8)
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

print("BFS Path from 1 to 8:")
path = bfs(graph, 1, 8)
print(" -> ".join(map(str, path)) if path else "No path found")
