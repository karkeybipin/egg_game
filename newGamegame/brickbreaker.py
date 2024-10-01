import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brick Breaker")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

paddle_width = 100
paddle_height = 15
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 50, paddle_width, paddle_height)

ball_radius = 10
ball_pos = [screen_width // 2, screen_height // 2]
ball_speed = [4, -4]

brick_width = 80
brick_height = 30
bricks = [pygame.Rect(10 + (brick_width + 10) * i, 10 + (brick_height + 10) * j, brick_width, brick_height) for i in range(8) for j in range(4)]

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-6, 0)
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.move_ip(6, 0)

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[0] <= ball_radius or ball_pos[0] >= screen_width - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= ball_radius:
        ball_speed[1] = -ball_speed[1]
    
    if paddle.collidepoint(ball_pos[0], ball_pos[1] + ball_radius):
        ball_speed[1] = -ball_speed[1]

    for brick in bricks[:]:
        if brick.collidepoint(ball_pos[0], ball_pos[1] - ball_radius):
            bricks.remove(brick)
            ball_speed[1] = -ball_speed[1]
            break

    if ball_pos[1] >= screen_height:
        font = pygame.font.SysFont(None, 74)
        text = font.render("Game Over", True, RED)
        screen.blit(text, (screen_width // 3, screen_height // 2 - 50))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.draw.rect(screen, BLACK, paddle)
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)

    for brick in bricks:
        pygame.draw.rect(screen, BLACK, brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
