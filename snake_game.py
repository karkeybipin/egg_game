import pygame
import time
import random
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 25)

def display_score(score):
    value = score_font.render(f"Score: {score}", True, BLACK)
    screen.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])


def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width // 6, screen_height // 3])


def game_loop():
    game_over = False
    game_close = False
    x = screen_width // 2
    y = screen_height // 2
    x_change = 0
    y_change = 0
    snake_list = []
    length_of_snake = 1
    food_x = round(random.randrange(
        0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(
        0, screen_height - snake_block) / 10.0) * 10.0
    while not game_over:
        while game_close:
            screen.fill(BLUE)
            display_message("You Lost! Press C-Play Again or Q-Quit", RED)
            display_score(length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        screen.fill(WHITE)
        pygame.draw.rect(
            screen, GREEN, [food_x, food_y, snake_block, snake_block])
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)
        pygame.display.update()
        if x == food_x and y == food_y:
            food_x = round(random.randrange(
                0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(
                0, screen_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_loop()
