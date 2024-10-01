import pygame
import math

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Throw the Ball into the Basket')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()

basket_img = pygame.image.load('basket.png')
basket_rect = basket_img.get_rect(center=(700, 400))

ball_radius = 20
ball_color = RED
ball_pos = [100, 500]
ball_velocity = [0, 0]
gravity = 0.5
is_dragging = False


def draw_basket():
    screen.blit(basket_img, basket_rect)


def throw_ball():
    global ball_velocity, is_dragging
    if not is_dragging:
        ball_velocity[1] += gravity
        ball_pos[0] += ball_velocity[0]
        ball_pos[1] += ball_velocity[1]


def check_basket():
    if basket_rect.collidepoint(ball_pos[0], ball_pos[1]):
        return True
    return False


running = True
while running:
    screen.fill(WHITE)

    draw_basket()

    pygame.draw.circle(screen, ball_color, (int(
        ball_pos[0]), int(ball_pos[1])), ball_radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if math.hypot(ball_pos[0] - event.pos[0], ball_pos[1] - event.pos[1]) < ball_radius:
                is_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if is_dragging:
                mouse_x, mouse_y = event.pos
                ball_velocity[0] = (mouse_x - ball_pos[0]) / 10
                ball_velocity[1] = (mouse_y - ball_pos[1]) / 10
                is_dragging = False
    throw_ball()

    if check_basket():
        pygame.display.set_caption('You Scored!')
    else:
        pygame.display.set_caption('Throw the Ball into the Basket')

    if ball_pos[0] < ball_radius or ball_pos[0] > screen_width - ball_radius:
        ball_velocity[0] *= -1
    if ball_pos[1] < ball_radius or ball_pos[1] > screen_height - ball_radius:
        ball_velocity[1] *= -0.8

    pygame.display.update()

    clock.tick(60)

pygame.quit()
