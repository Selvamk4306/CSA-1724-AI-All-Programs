from collections import deque

def is_valid(m, c):
    return (m == 0 or m >= c) and (3 - m == 0 or (3 - m) >= (3 - c))

def get_successors(state):
    m, c, boat = state
    moves = [
        (1, 0, "1 Missionary"),
        (2, 0, "2 Missionaries"),
        (0, 1, "1 Cannibal"),
        (0, 2, "2 Cannibals"),
        (1, 1, "1 Missionary and 1 Cannibal")
    ]
    successors = []
    for dm, dc, desc in moves:
        if boat == 'left':
            new_m, new_c = m - dm, c - dc
            new_boat = 'right'
        else:
            new_m, new_c = m + dm, c + dc
            new_boat = 'left'
        if 0 <= new_m <= 3 and 0 <= new_c <= 3 and is_valid(new_m, new_c):
            successors.append(((new_m, new_c, new_boat), desc))
    return successors

def bfs(start, goal):
    queue = deque()
    queue.append((start, [start], []))
    visited = set()
    visited.add(start)

    while queue:
        state, path, actions = queue.popleft()
        if state == goal:
            return path, actions
        for succ, move_desc in get_successors(state):
            if succ not in visited:
                visited.add(succ)
                queue.append((succ, path + [succ], actions + [move_desc]))
    return None, None

# Initial and goal states
start_state = (3, 3, 'left')
goal_state = (0, 0, 'right')

solution_path, solution_moves = bfs(start_state, goal_state)

if solution_path:
    print("Solution steps with moves:")
    for i in range(len(solution_moves)):
        current = solution_path[i]
        next_state = solution_path[i + 1]
        print(f"Step {i+1}: Move {solution_moves[i]} from {current} to {next_state}")
    print(f"Goal reached at: {solution_path[-1]}")
else:
    print("No solution found.")