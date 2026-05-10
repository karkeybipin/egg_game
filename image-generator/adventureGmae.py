def intro():
    print("Welcome, adventurer! You find yourself in a dark cave. There are two paths ahead.")
    print("You can go 'left' or 'right'. Choose wisely.")

def left_path():
    print("You took the left path and encountered a sleeping dragon.")
    choice = input("Do you 'sneak' past the dragon or 'fight' it? ").lower()

    if choice == "sneak":
        print("You carefully sneak past the dragon and find a chest full of gold. You win!")
    elif choice == "fight":
        print("You try to fight the dragon but it wakes up and burns you to ashes. Game over.")
    else:
        print("Invalid choice. You stand frozen, and the dragon wakes up. Game over.")

def right_path():
    print("You took the right path and find a treasure chest.")
    choice = input("Do you want to 'open' the chest or 'ignore' it? ").lower()

    if choice == "open":
        print("You open the chest and find a magical sword. You win!")
    elif choice == "ignore":
        print("You ignore the chest and continue walking, only to fall into a pit. Game over.")
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
