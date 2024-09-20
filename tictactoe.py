board = [' ' for _ in range(9)]


def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                      (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def check_tie():
    return ' ' not in board


def tic_tac_toe():
    current_player = 'X'
    while True:
        print_board()
        try:
            move = int(
                input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("That spot is already taken, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")
            continue
        board[move] = current_player
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_tie():
            print_board()
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'


tic_tac_toe()
