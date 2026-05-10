import random

def print_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--+---+--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--+---+--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def check_winner(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))

def is_board_full(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

def player_move(board):
    move = 0
    while move not in range(1, 10) or board[move] != ' ':
        move = int(input("Enter your move (1-9): "))
    board[move] = 'X'

def computer_move(board):
    move = random.randint(1, 9)
    while board[move] != ' ':
        move = random.randint(1, 9)
    board[move] = 'O'

def play_game():
    board = [' '] * 10
    print("Welcome to Tic-Tac-Toe")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        computer_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

play_game()
