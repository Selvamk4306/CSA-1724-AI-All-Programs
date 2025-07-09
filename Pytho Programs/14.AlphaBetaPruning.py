import math

# Example game tree values (for leaf nodes)
game_tree = [3, 5, 6, 9, 1, 2, 0, -1]


# Minimax function with alpha-beta pruning
def alphabeta(depth, node_index, is_max, values, alpha, beta):
    # Terminal condition: leaf node is reached
    if depth == 3:
        return values[node_index]

    if is_max:
        best = -math.inf

        # Recur for left and right children
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf

        # Recur for left and right children
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best


if __name__ == "__main__":
    print("Optimal value is:", alphabeta(0, 0, True, game_tree, -math.inf, math.inf))
