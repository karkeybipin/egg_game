import random
import time

def bottle_flicker_game(players):
    print("Spinning the bottle...")
    
    # Simulate spinning effect
    for _ in range(5):
        print(".", end='', flush=True)
        time.sleep(0.5)

    # Select a random player
    chosen_player = random.choice(players)
    print(f"\nThe bottle points to: {chosen_player}!")

def main():
    print("Welcome to the Bottle Flicker Game!")
    
    # Get player names
    players = []
    num_players = int(input("How many players are playing? "))

    for i in range(num_players):
        name = input(f"Enter name of player {i+1}: ")
        players.append(name)

    # Start the game loop
    while True:
        # Play a round
        bottle_flicker_game(players)

        # Ask if they want to play another round
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()

        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
