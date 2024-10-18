import random
COLORS = ['Red', 'Green', 'Blue', 'Yellow']
VALUES = [str(i) for i in range(1, 10)] + ['Skip', 'Reverse', 'Draw Two']


class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"


class Player:
    def __init__(self, name, is_human=False):
        self.name = name
        self.hand = []
        self.is_human = is_human

    def draw_card(self, deck):
        card = deck.draw()
        self.hand.append(card)
        return card

    def play_card(self, top_card):
        playable_cards = [card for card in self.hand if card.color ==
                          top_card.color or card.value == top_card.value]

        if self.is_human:
            print(f"\nYour turn! Top card is {top_card}")
            print("Your hand: ")
            for idx, card in enumerate(self.hand):
                print(f"{idx+1}: {card}")
            choice = int(
                input("Pick a card to play (number), or 0 to draw a card: "))

            if choice == 0:
                return None
            else:
                chosen_card = self.hand.pop(choice - 1)
                return chosen_card
        else:
            if playable_cards:
                return self.hand.pop(self.hand.index(random.choice(playable_cards)))
            else:
                return None


class Deck:
    def __init__(self):
        self.cards = [Card(color, value)
                      for color in COLORS for value in VALUES]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


def initialize_game():
    deck = Deck()
    players = [Player(f"AI Player {i+1}") for i in range(4)]
    human_player = Player("Human Player", is_human=True)
    players.insert(0, human_player)
    for player in players:
        for _ in range(7):
            player.draw_card(deck)
    top_card = deck.draw()
    return deck, players, top_card


def play_game():
    deck, players, top_card = initialize_game()
    current_player_index = 0
    direction = 1
    while True:
        current_player = players[current_player_index]
        print(f"\n{current_player.name}'s turn.")
        played_card = current_player.play_card(top_card)
        if played_card:
            print(f"{current_player.name} played {played_card}")
            top_card = played_card
        else:
            new_card = current_player.draw_card(deck)
            print(f"{current_player.name} drew a card: {new_card}")

        if not current_player.hand:
            print(f"\n{current_player.name} wins the game!")
            break
        current_player_index = (current_player_index + direction) % 5


if __name__ == "__main__":
    play_game()
