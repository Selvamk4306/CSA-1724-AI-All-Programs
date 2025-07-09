from collections import deque

def bfs(graph, start):
    visited = set()              # To keep track of visited nodes
    queue = deque([start])       # Queue for BFS, initialized with the start node

    print("BFS Traversal Order:")
    while queue:
        vertex = queue.popleft() # Dequeue the next node

        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)

            # Enqueue all adjacent (neighboring) vertices that haven't been visited
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:
graph = {
    'A': ['B', 'E'],
    'B': ['A', 'D', 'C'],
    'E': ['A', 'F'],
    'D': ['B'],
    'C': ['B'],
    'F': ['E']
}

start_node = 'A'
bfs(graph, start_node)