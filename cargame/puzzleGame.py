import random

PUZZLE_SIZE = 3
EMPTY_TILE = PUZZLE_SIZE * PUZZLE_SIZE

def create_puzzle():
    numbers = list(range(1, EMPTY_TILE)) + [EMPTY_TILE]
    random.shuffle(numbers)
    return [numbers[i:i + PUZZLE_SIZE] for i in range(0, len(numbers), PUZZLE_SIZE)]

def find_empty_tile(puzzle):
    for i in range(PUZZLE_SIZE):
        for j in range(PUZZLE_SIZE):
            if puzzle[i][j] == EMPTY_TILE:
                return i, j

def is_solved(puzzle):
    solution = list(range(1, EMPTY_TILE)) + [EMPTY_TILE]
    return puzzle == [solution[i:i + PUZZLE_SIZE] for i in range(0, len(solution), PUZZLE_SIZE)]

def print_puzzle(puzzle):
    for row in puzzle:
        print(" | ".join(str(x) if x != EMPTY_TILE else " " for x in row))
        print("-" * (PUZZLE_SIZE * 4 - 1))

def move_tile(puzzle, direction):
    empty_row, empty_col = find_empty_tile(puzzle)

    if direction == "up" and empty_row < PUZZLE_SIZE - 1:
        puzzle[empty_row][empty_col], puzzle[empty_row + 1][empty_col] = puzzle[empty_row + 1][empty_col], puzzle[empty_row][empty_col]
    elif direction == "down" and empty_row > 0:
        puzzle[empty_row][empty_col], puzzle[empty_row - 1][empty_col] = puzzle[empty_row - 1][empty_col], puzzle[empty_row][empty_col]
    elif direction == "left" and empty_col < PUZZLE_SIZE - 1:
        puzzle[empty_row][empty_col], puzzle[empty_row][empty_col + 1] = puzzle[empty_row][empty_col + 1], puzzle[empty_row][empty_col]
    elif direction == "right" and empty_col > 0:
        puzzle[empty_row][empty_col], puzzle[empty_row][empty_col - 1] = puzzle[empty_row][empty_col - 1], puzzle[empty_row][empty_col]
    else:
        print("Invalid move!")

def puzzle_game():
    puzzle = create_puzzle()
    print("Welcome to the sliding puzzle game!")
    print("Arrange the numbers in order by sliding the tiles into the empty space.")
    print("Use 'up', 'down', 'left', or 'right' to move a tile.")
    print_puzzle(puzzle)

    while not is_solved(puzzle):
        move = input("Enter your move (up, down, left, right): ").lower()
        move_tile(puzzle, move)
        print_puzzle(puzzle)

    print("Congratulations! You solved the puzzle.")

if __name__ == "__main__":
    puzzle_game()

