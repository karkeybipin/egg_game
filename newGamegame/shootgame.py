import pygame
import random
import math

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball Shooting Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

shooter_pos = [screen_width // 2, screen_height - 50]
shooter_radius = 30
shoot_speed = 10
bullets = []
target_radius = 20
targets = []
score = 0
game_over = False

clock = pygame.time.Clock()

def create_targets():
    for _ in range(5):
        x = random.randint(0, screen_width - target_radius)
        y = random.randint(0, screen_height // 2)
        targets.append([x, y])

def check_hit(bullet):
    global score
    for target in targets[:]:
        if math.hypot(bullet[0] - target[0], bullet[1] - target[1]) < target_radius:
            targets.remove(target)
            score += 1
            return True
    return False

create_targets()
while not game_over:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([shooter_pos[0], shooter_pos[1] - shooter_radius])

    pygame.draw.circle(screen, GREEN, shooter_pos, shooter_radius)

    for bullet in bullets[:]:
        bullet[1] -= shoot_speed
        pygame.draw.circle(screen, RED, bullet, 5)
        if bullet[1] < 0 or check_hit(bullet):
            bullets.remove(bullet)

    for target in targets:
        pygame.draw.circle(screen, BLACK, target, target_radius)

    if not targets:
        create_targets()

    font = pygame.font.SysFont(None, 55)
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
