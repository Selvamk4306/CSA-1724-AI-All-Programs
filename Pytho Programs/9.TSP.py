import itertools

def travelling_salesman(graph, start):
    # List of cities excluding the starting city
    cities = list(graph.keys())
    cities.remove(start)

    min_path = None
    min_cost = float('inf')

    # Try all permutations of cities
    for perm in itertools.permutations(cities):
        current_cost = 0
        current_city = start

        # Visit each city in the permutation
        for next_city in perm:
            current_cost += graph[current_city][next_city]
            current_city = next_city

        # Return to the start city
        current_cost += graph[current_city][start]

        # Check if this path is better
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = (start,) + perm + (start,)

    print("Minimum cost path:", " -> ".join(min_path))
    print("Minimum cost:", min_cost)

# Sample graph represented as a distance matrix
graph = {
    'A': {'A': 0, 'B': 7, 'C': 9, 'D': 13},
    'B': {'A': 7, 'B': 0, 'C': 10, 'D': 5},
    'C': {'A': 9, 'B': 10, 'C': 0, 'D': 11},
    'D': {'A': 13, 'B': 5, 'C': 11, 'D': 0}
}

travelling_salesman(graph, 'A')