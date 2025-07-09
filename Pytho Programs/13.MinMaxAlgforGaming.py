# Define a simple static game tree:
#            MAX
#         /       \
#       MIN        MIN
#     /   \      /     \
#    3     5    2       9

# The MAX player will pick the move that gives the highest score,
# while the MIN player picks the move that gives the lowest score.


def minimax(depth, is_maximizing, values, index):
    # If we're at leaf node (depth == 2), return the value
    if depth == 2:
        return values[index]

    if is_maximizing:
        # MAX level
        best = float('-inf')
        # Left child
        val1 = minimax(depth + 1, False, values, index * 2)
        # Right child
        val2 = minimax(depth + 1, False, values, index * 2 + 1)
        best = max(val1, val2)
        return best
    else:
        # MIN level
        best = float('inf')
        # Left child
        val1 = minimax(depth + 1, True, values, index * 2)
        # Right child
        val2 = minimax(depth + 1, True, values, index * 2 + 1)
        best = min(val1, val2)
        return best


# Leaf values of the tree: left to right
leaf_values = [3, 5, 2, 9]

# Start from root at depth 0, index 0
optimal_value = minimax(0, True, leaf_values, 0)

print("The optimal value is:", optimal_value)
