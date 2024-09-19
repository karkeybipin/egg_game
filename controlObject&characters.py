import pygame
import random
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
player_width = 50
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
block_width = 50
block_height = 50
block_speed = 5
block_list = []
font = pygame.font.SysFont(None, 55)


def display_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, [10, 10])


def game_loop():
    game_over = False
    clock = pygame.time.Clock()
    player_x = screen_width // 2 - player_width // 2
    block_list.clear()
    score = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        if random.randint(1, 50) == 1:
            block_x = random.randint(0, screen_width - block_width)
            block_y = -block_height
            block_list.append([block_x, block_y])
        for block in block_list:
            block[1] += block_speed
            if block[1] > screen_height:
                block_list.remove(block)
                score += 1
        for block in block_list:
            if (block[0] < player_x < block[0] + block_width or block[0] < player_x + player_width < block[0] + block_width) and \
               (block[1] < player_y < block[1] + block_height or block[1] < player_y + player_height < block[1] + block_height):
                game_over = True
        screen.fill(WHITE)
        pygame.draw.rect(
            screen, BLACK, [player_x, player_y, player_width, player_height])
        for block in block_list:
            pygame.draw.rect(
                screen, RED, [block[0], block[1], block_width, block_height])
        display_score(score)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


game_loop()
