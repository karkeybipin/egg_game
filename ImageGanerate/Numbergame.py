import random

def get_guess(tries, number_range):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {number_range}: "))
            return guess
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {number_range}.")

def play_game():
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

    if difficulty == "easy":
        number_range = 10
        tries = 5
    elif difficulty == "medium":
        number_range = 50
        tries = 7
    elif difficulty == "hard":
        number_range = 100
        tries = 10
    else:
        print("Invalid difficulty. Defaulting to easy.")
        number_range = 10
        tries = 5

    target_number = random.randint(1, number_range)
    print(f"You have {tries} tries to guess the number between 1 and {number_range}.")

    while tries > 0:
        guess = get_guess(tries, number_range)

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {target_number}.")
            return

        tries -= 1
        print(f"You have {tries} tries left.")

    print(f"Game Over! The number was {target_number}.")

play_game()
