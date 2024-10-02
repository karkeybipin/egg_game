import random
import time


def bottle_flicker_game(players):
    print("Welcome to the Bottle Flicker Game!")
    print("Players:", players)
    print("Spinning the bottle...")

    for _ in range(5):
        print(".", end='', flush=True)
        time.sleep(0.5)
    chosen_player = random.choice(players)
    print(f"\nThe bottle points to: {chosen_player}!")


players = ["Ramu Ji",  "Hari Ji"]

bottle_flicker_game(players)
