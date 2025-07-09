import heapq

def a_star(graph, heuristics, start, goal):
    # Priority queue: (f_cost, current_node, path, g_cost)
    open_list = [(heuristics[start], start, [start], 0)]
    visited = set()

    while open_list:
        f, current, path, g = heapq.heappop(open_list)

        if current == goal:
            print("Shortest path:", " -> ".join(path))
            print("Total cost:", g-1)
            return

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristics[neighbor]
                heapq.heappush(open_list, (new_f, neighbor, path + [neighbor], new_g))

    print("No path found.")

# Sample graph (with actual costs)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

# Heuristic values (estimated cost to goal 'E')
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

# Run A*
a_star(graph, heuristics, 'A', 'E')
      