# import random
# COLORS = ['Red', 'Green', 'Blue', 'Yellow']
# VALUES = [str(i) for i in range(1, 10)] + ['Skip', 'Reverse', 'Draw Two']


# class Card:
#     def __init__(self, color, value):
#         self.color = color
#         self.value = value

#     def __str__(self):
#         return f"{self.color} {self.value}"


# class Player:
#     def __init__(self, name, is_human=False):
#         self.name = name
#         self.hand = []
#         self.is_human = is_human

#     def draw_card(self, deck):
#         card = deck.draw()
#         self.hand.append(card)
#         return card

#     def play_card(self, top_card):
#         playable_cards = [card for card in self.hand if card.color ==
#                           top_card.color or card.value == top_card.value]

#         if self.is_human:
#             print(f"\nYour turn! Top card is {top_card}")
#             print("Your hand: ")
#             for idx, card in enumerate(self.hand):
#                 print(f"{idx+1}: {card}")
#             choice = int(
#                 input("Pick a card to play (number), or 0 to draw a card: "))

#             if choice == 0:
#                 return None
#             else:
#                 chosen_card = self.hand.pop(choice - 1)
#                 return chosen_card
#         else:
#             if playable_cards:
#                 return self.hand.pop(self.hand.index(random.choice(playable_cards)))
#             else:
#                 return None


# class Deck:
#     def __init__(self):
#         self.cards = [Card(color, value)
#                       for color in COLORS for value in VALUES]
#         random.shuffle(self.cards)

#     def draw(self):
#         return self.cards.pop()


# def initialize_game():
#     deck = Deck()
#     players = [Player(f"AI Player {i+1}") for i in range(4)]
#     human_player = Player("Human Player", is_human=True)
#     players.insert(0, human_player)
#     for player in players:
#         for _ in range(7):
#             player.draw_card(deck)
#     top_card = deck.draw()
#     return deck, players, top_card


# def play_game():
#     deck, players, top_card = initialize_game()
#     current_player_index = 0
#     direction = 1
#     while True:
#         current_player = players[current_player_index]
#         print(f"\n{current_player.name}'s turn.")
#         played_card = current_player.play_card(top_card)
#         if played_card:
#             print(f"{current_player.name} played {played_card}")
#             top_card = played_card
#         else:
#             new_card = current_player.draw_card(deck)
#             print(f"{current_player.name} drew a card: {new_card}")

#         if not current_player.hand:
#             print(f"\n{current_player.name} wins the game!")
#             break
#         current_player_index = (current_player_index + direction) % 5


# if __name__ == "__main__":
#     play_game()


# import pygame
# import random
# pygame.init()
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("UNO Game")
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# font = pygame.font.Font(None, 36)


# class Card:
#     def __init__(self, color, value):
#         self.color = color
#         self.value = value
#         self.rect = pygame.Rect(0, 0, 60, 90)

#     def draw(self, screen, x, y):
#         pygame.draw.rect(screen, self.color, (x, y, 60, 90))
#         pygame.draw.rect(screen, BLACK, (x, y, 60, 90), 2)
#         value_text = font.render(self.value, True, BLACK)
#         screen.blit(value_text, (x + 10, y + 30))

#     def is_clicked(self, mouse_pos):
#         return self.rect.collidepoint(mouse_pos)


# class Player:
#     def __init__(self, name, is_human=False):
#         self.name = name
#         self.hand = []
#         self.is_human = is_human

#     def draw_card(self, deck):
#         card = deck.draw()
#         self.hand.append(card)

#     def play_card(self, top_card):
#         playable_cards = [card for card in self.hand if card.color ==
#                           top_card.color or card.value == top_card.value]
#         if self.is_human:
#             return playable_cards
#         else:
#             return random.choice(playable_cards) if playable_cards else None


# class Deck:
#     def __init__(self):
#         colors = [RED, GREEN, BLUE, YELLOW]
#         values = [str(i) for i in range(1, 10)] + \
#             ['Skip', 'Reverse', 'Draw Two']
#         self.cards = [Card(color, value)
#                       for color in colors for value in values]
#         random.shuffle(self.cards)

#     def draw(self):
#         return self.cards.pop()


# def initialize_game():
#     deck = Deck()
#     players = [Player(f"AI Player {i+1}") for i in range(4)]
#     human_player = Player("Human Player", is_human=True)
#     players.insert(0, human_player)
#     for player in players:
#         for _ in range(7):
#             player.draw_card(deck)
#     top_card = deck.draw()
#     return deck, players, top_card


# def play_game():
#     deck, players, top_card = initialize_game()
#     current_player_index = 0
#     running = True
#     while running:
#         screen.fill(WHITE)
#         top_card.draw(screen, SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 45)
#         human_player = players[0]
#         for i, card in enumerate(human_player.hand):
#             card.rect.topleft = (100 + i * 70, SCREEN_HEIGHT - 100)
#             card.draw(screen, 100 + i * 70, SCREEN_HEIGHT - 100)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = event.pos
#                 for card in human_player.hand:
#                     if card.is_clicked(mouse_pos):
#                         if card.color == top_card.color or card.value == top_card.value:
#                             top_card = card
#                             human_player.hand.remove(card)
#                             current_player_index = (
#                                 current_player_index + 1) % 5
#                             break
#         pygame.display.flip()


# if __name__ == "__main__":
#     play_game()
#     pygame.quit()


import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("UNO Game")
GREEN_BACKGROUND = (0, 128, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 36)


class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.rect = pygame.Rect(0, 0, 60, 90)

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, self.color, (x, y, 60, 90))
        pygame.draw.rect(screen, BLACK, (x, y, 60, 90), 2)
        value_text = font.render(self.value, True, BLACK)
        screen.blit(value_text, (x + 10, y + 30))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


class Player:
    def __init__(self, name, is_human=False):
        self.name = name
        self.hand = []
        self.is_human = is_human

    def draw_card(self, deck):
        card = deck.draw()
        self.hand.append(card)

    def play_card(self, top_card):
        playable_cards = [card for card in self.hand if card.color ==
                          top_card.color or card.value == top_card.value]
        if self.is_human:
            return playable_cards
        else:
            return random.choice(playable_cards) if playable_cards else None


class Deck:
    def __init__(self):
        colors = [RED, GREEN, BLUE, YELLOW]
        values = [str(i) for i in range(1, 10)] + \
            ['Skip', 'Reverse', 'Draw Two']
        self.cards = [Card(color, value)
                      for color in colors for value in values]
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


def draw_players(players, top_card):
    human_player = players[0]
    for i, player in enumerate(players[1:], start=1):
        y_pos = 50 + (i - 1) * 150
        for j, card in enumerate(player.hand):
            card.draw(screen, 100 + j * 70, y_pos)
    for i, card in enumerate(human_player.hand):
        card.rect.topleft = (100 + i * 70, SCREEN_HEIGHT - 100)
        card.draw(screen, 100 + i * 70, SCREEN_HEIGHT - 100)
    top_card.draw(screen, SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 - 45)


def play_game():
    deck, players, top_card = initialize_game()
    current_player_index = 0
    running = True

    while running:
        screen.fill(GREEN_BACKGROUND)

        pygame.draw.rect(
            screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 15)

        draw_players(players, top_card)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if current_player_index == 0:
                    mouse_pos = event.pos
                    human_player = players[0]
                    for card in human_player.hand:
                        if card.is_clicked(mouse_pos):
                            if card.color == top_card.color or card.value == top_card.value:
                                top_card = card
                                human_player.hand.remove(card)
                                current_player_index = (
                                    current_player_index + 1) % 5
                                break

        if current_player_index != 0:
            ai_player = players[current_player_index]
            played_card = ai_player.play_card(top_card)
            if played_card:
                top_card = played_card
                ai_player.hand.remove(played_card)
            else:
                ai_player.draw_card(deck)
            current_player_index = (current_player_index + 1) % 5

        pygame.display.flip()


if __name__ == "__main__":
    play_game()
    pygame.quit()
