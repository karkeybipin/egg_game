import random


def intro():
    print("Welcome, adventurer! You find yourself in a dark cave. There are two paths ahead.")
    print("You can go 'left' or 'right'. Choose wisely.")


def left_path():
    print("You took the left path and encountered a sleeping dragon.")
    choice = input("Do you 'sneak' past the dragon or 'fight' it? ").lower()

    if choice == "sneak":
        print("You carefully sneak past the dragon and find a chest full of gold. You win!")
    elif choice == "fight":
        print(
            "You try to fight the dragon but it wakes up and burns you to ashes. Game over.")
    else:
        print("Invalid choice. You stand frozen, and the dragon wakes up. Game over.")
# def intro():
#     print("Welcome, adventurer! You find yourself in a dark cave. There are two paths ahead.")
#     print("You can go 'left' or 'right'. Choose wisely.")

# def left_path():
#     print("You took the left path and encountered a sleeping dragon.")
#     choice = input("Do you 'sneak' past the dragon or 'fight' it? ").lower()

#     if choice == "sneak":
#         print("You carefully sneak past the dragon and find a chest full of gold. You win!")
#     elif choice == "fight":
#         print("You try to fight the dragon but it wakes up and burns you to ashes. Game over.")
#     else:
#         print("Invalid choice. You stand frozen, and the dragon wakes up. Game over.")

# def right_path():
#     print("You took the right path and find a treasure chest.")
#     choice = input("Do you want to 'open' the chest or 'ignore' it? ").lower()

#     if choice == "open":
#         print("You open the chest and find a magical sword. You win!")
#     elif choice == "ignore":
#         print("You ignore the chest and continue walking, only to fall into a pit. Game over.")
#     else:
#         print("Invalid choice. You trip over a rock and fall into the pit. Game over.")

# def play_game():
#     intro()
#     path = input("Which path will you choose? ").lower()

#     if path == "left":
#         left_path()
#     elif path == "right":
#         right_path()
#     else:
#         print("Invalid choice. You wander aimlessly and eventually starve. Game over.")

# play_game()


def right_path():
    print("You took the right path and find a treasure chest.")
    choice = input("Do you want to 'open' the chest or 'ignore' it? ").lower()

    if choice == "open":
        print("You open the chest and find a magical sword. You win!")
    elif choice == "ignore":
        print(
            "You ignore the chest and continue walking, only to fall into a pit. Game over.")
    else:
        print("Invalid choice. You trip over a rock and fall into the pit. Game over.")


def play_game():
    intro()
    path = input("Which path will you choose? ").lower()

    if path == "left":
        left_path()
    elif path == "right":
        right_path()
    else:
        print("Invalid choice. You wander aimlessly and eventually starve. Game over.")


play_game()




#idea
# game-Numberguessing

# def get_guess(tries, number_range):
#     while True:
#         try:
#             guess = int(
#                 input(f"Guess a number between 1 and {number_range}: "))
#             return guess
#         except ValueError:
#             print(f"Invalid input. Please enter a number between 1 and {
#                   number_range}.")


# def play_game():
#     difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

#     if difficulty == "easy":
#         number_range = 10
#         tries = 5
#     elif difficulty == "medium":
#         number_range = 50
#         tries = 7
#     elif difficulty == "hard":
#         number_range = 100
#         tries = 10
#     else:
#         print("Invalid difficulty. Defaulting to easy.")
#         number_range = 10
#         tries = 5

#     target_number = random.randint(1, number_range)
#     print(f"You have {tries} tries to guess the number between 1 and {
#           number_range}.")

#     while tries > 0:
#         guess = get_guess(tries, number_range)

#         if guess < target_number:
#             print("Too low!")
#         elif guess > target_number:
#             print("Too high!")
#         else:
#             print(f"Congratulations! You guessed the number {target_number}.")
#             return

#         tries -= 1
#         print(f"You have {tries} tries left.")

#     print(f"Game Over! The number was {target_number}.")


# play_game()
