# Tic-Tac-Toe Game in Python

# Initialize the board
board = [' ' for _ in range(9)]

# Function to display the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check for a win
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), 
                      (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

# Function to check for a tie
def check_tie():
    return ' ' not in board

# Main game loop
def tic_tac_toe():
    current_player = 'X'
    
    while True:
        print_board()
        
        # Get input from player
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("That spot is already taken, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")
            continue
        
        # Update board
        board[move] = current_player
        
        # Check for a win or a tie
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_tie():
            print_board()
            print("It's a tie!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
tic_tac_toe()
