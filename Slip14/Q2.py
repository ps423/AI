'''
Q.2) Write a program to implement Iterative Deepening DFS algorithm. [Goal Node = G]
[20 Marks]
'''

def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        result = dls(graph, start, goal, depth, visited)
        if result is not None:
            return result
    return None

def dls(graph, node, goal, depth, visited):
    if node == goal:
        return [node]
    
    if depth <= 0:
        return None
    
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dls(graph, neighbor, goal, depth - 1, visited)
            if result is not None:
                return [node] + result
    
    return None

# Example graph (Goal Node = G)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['G'],
    'G': [],
    'H': [],
    'I': [],
    'K': []
}

print("Iterative Deepening DFS from A to G:")
path = iddfs(graph, 'A', 'G', 4)
print(" -> ".join(path) if path else "No path found")
