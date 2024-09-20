import random

def hot_or_cold(guess, target):
    """Returns a clue based on how close the guess is to the target number."""
    difference = abs(target - guess)
    if difference == 0:
        return "Correct!"
    elif difference <= 2:
        return "Boiling hot!"
    elif difference <= 5:
        return "Very hot!"
    elif difference <= 10:
        return "Warm"
    elif difference <= 20:
        return "Cold"
    else:
        return "Freezing cold!"

def number_guessing_game():
    print("Welcome to the 'Hot and Cold Number Guessing' game!")
    print("I have selected a random number between 1 and 100.")
    print("You have 10 attempts to guess the number correctly.\n")

    target_number = random.randint(1, 100)
    attempts = 10

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        clue = hot_or_cold(guess, target_number)
        print(clue)
        
        if clue == "Correct!":
            print(f"Congratulations! You guessed the correct number {target_number} in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all {attempts} attempts. The correct number was {target_number}.")

# Run the game
number_guessing_game()
