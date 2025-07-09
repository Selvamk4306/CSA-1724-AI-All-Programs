from collections import deque

# Function to print the path from initial state to goal state
def print_path(path):
    print("Solution path:")
    for state in path:
        print(f"Jug1: {state[0]}L, Jug2: {state[1]}L")

# Function to solve the water jug problem using BFS
def water_jug_bfs(jug1_capacity, jug2_capacity, goal_state):
    visited = set()
    queue = deque()
    
    # Initial state: both jugs empty
    queue.append([(0, 0)])

    while queue:
        path = queue.popleft()
        current_state = path[-1]

        # Check if goal is reached (e.g., Jug1 = 2L and Jug2 = 0L)
        if current_state == goal_state:
            print_path(path)
            return

        if current_state in visited:
            continue

        visited.add(current_state)

        x, y = current_state
        possible_states = []

        # Fill Jug1
        possible_states.append((jug1_capacity, y))

        # Fill Jug2
        possible_states.append((x, jug2_capacity))

        # Empty Jug1
        possible_states.append((0, y))

        # Empty Jug2
        possible_states.append((x, 0))

        # Pour Jug1 -> Jug2
        pour = min(x, jug2_capacity - y)
        possible_states.append((x - pour, y + pour))

        # Pour Jug2 -> Jug1
        pour = min(y, jug1_capacity - x)
        possible_states.append((x + pour, y - pour))

        for state in possible_states:
            if state not in visited:
                new_path = list(path)
                new_path.append(state)
                queue.append(new_path)

    print("No solution found.")

# Input capacities and goal state
jug1_capacity = 4
jug2_capacity = 3
goal_state = (2, 0)

# Call the function
water_jug_bfs(jug1_capacity, jug2_capacity, goal_state)