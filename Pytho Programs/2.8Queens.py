# Size of the chessboard
N = 8

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Function to check if placing a queen is safe
def is_safe(board, row, col):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

# Function to solve the problem using backtracking
def solve(board, row):
    if row == N:
        print_board(board)
        return True  # return True to stop at the first solution
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 'Q'  # Place queen
            if solve(board, row + 1):  # Recur to place next queen
                return True
            board[row][col] = '.'  # Backtrack
    return False

# Initialize the board
board = [['.' for _ in range(N)] for _ in range(N)]

# Solve the problem
if solve(board, 0):
    print("Solution found.")
else:
    print("Not found the Solution")