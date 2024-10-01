import pygame
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Click the Moving Squares")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

square_size = 30
squares = []
score = 0

def create_squares(num_squares):
    for _ in range(num_squares):
        x = random.randint(0, screen_width - square_size)
        y = random.randint(0, screen_height - square_size)
        vx = random.choice([-3, 3])
        vy = random.choice([-3, 3])
        squares.append(pygame.Rect(x, y, square_size, square_size))

create_squares(5)
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for square in squares[:]:
                if square.collidepoint(event.pos):
                    squares.remove(square)
                    score += 1

    for square in squares:
        square.move_ip(random.choice([-2, 2]), random.choice([-2, 2]))
        pygame.draw.rect(screen, RED, square)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    pygame.time.delay(50)

pygame.quit()
