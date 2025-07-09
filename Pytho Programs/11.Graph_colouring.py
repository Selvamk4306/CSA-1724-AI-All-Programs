import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(bo, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(bo[i] == player for i in combo) for combo in win_combinations)

def is_board_full():
    return ' ' not in board

def get_available_moves():
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(is_maximizing):
    if is_winner(board, 'X'):
        return 1         # Human wins → best for Human
    elif is_winner(board, 'O'):
        return -1        # AI wins → worst for Human
    elif is_board_full():
        return 0         # Draw

    if is_maximizing:  # Human's turn (maximize score)
        best_score = -math.inf
        for move in get_available_moves():
            board[move] = 'X'
            score = minimax(False)       # AI's turn next
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:              # AI's turn (minimize score)
        best_score = math.inf
        for move in get_available_moves():
            board[move] = 'O'
            score = minimax(True)        # Human's turn next
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = math.inf  # Minimize because AI is now minimizing
    move = -1
    for i in get_available_moves():
        board[i] = 'O'
        score = minimax(True)  # Human's move next
        board[i] = ' '
        if score < best_score:
            best_score = score
            move = i
    return move

def play_game():
    print("Tic Tac Toe: You (X) vs AI (O)")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue
        board[move] = 'X'
        print_board()
        if is_winner(board, 'X'):
            print("You win!")
            break
        if is_board_full():
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = 'O'
        print("AI's move:")
        print_board()
        if is_winner(board, 'O'):
            print("AI wins!")
            break
        if is_board_full():
            print("It's a draw!")
            break

# Run the game
play_game()