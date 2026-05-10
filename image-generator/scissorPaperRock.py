import random

def play_game():
    user_score = 0
    computer_score = 0
    options = ["rock", "paper", "scissors"]

    while True:
        user_input = input("Enter rock, paper, scissors or 'quit' to stop: ").lower()
        if user_input == "quit":
            break

        if user_input not in options:
            print("Invalid choice, try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose {computer_choice}")

        if user_input == computer_choice:
            print("It's a tie!")
        elif (user_input == "rock" and computer_choice == "scissors") or \
             (user_input == "paper" and computer_choice == "rock") or \
             (user_input == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score: You {user_score}, Computer {computer_score}")

    print("Final Score:")
    print(f"You: {user_score}, Computer: {computer_score}")
    print("Goodbye!")

play_game()
