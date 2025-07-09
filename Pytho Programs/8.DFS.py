def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            # Add unvisited neighbors to the stack
            stack.extend(reversed(graph[vertex]))  # reverse to mimic recursive DFS order

# Sample graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['E'],
    'E': ['C'],
    'F': ['G'],
    'G': []
}

print("DFS traversal starting from A:")
dfs(graph, 'A')