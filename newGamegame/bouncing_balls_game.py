import pygame
import random
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

ball_radius = 20
balls = []
gravity = 0.2
speed_increase = 0.05  
time_spent = 0  

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-4, 4)  
        self.vy = random.uniform(-4, 4)  
        self.color = random.choice([RED, BLUE])

    def move(self):
        self.vy += gravity
        self.x += self.vx
        self.y += self.vy

        if self.x < ball_radius or self.x > screen_width - ball_radius:
            self.vx *= -1

        if self.y < ball_radius or self.y > screen_height - ball_radius:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), ball_radius)

def create_balls(num_balls):
    for _ in range(num_balls):
        x = random.randint(ball_radius, screen_width - ball_radius)
        y = random.randint(ball_radius, screen_height - ball_radius)
        balls.append(Ball(x, y))

def game_over():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 74)
    text = font.render('Game Over', True, RED)
    screen.blit(text, (screen_width // 3, screen_height // 2 - 50))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def main():
    global time_spent
    clock = pygame.time.Clock()
    game_running = True

    num_balls = int(input("Enter the number of balls: "))
    create_balls(num_balls)

    while game_running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        all_stopped = True
        for ball in balls:
            if abs(ball.vx) > 0.1 or abs(ball.vy) > 0.1:
                all_stopped = False
            ball.move()
            ball.draw()

        if all_stopped:
            game_over()

        time_spent += clock.get_time() / 1000  
        for ball in balls:
            ball.vx += speed_increase * (1 if ball.vx > 0 else -1)
            ball.vy += speed_increase * (1 if ball.vy > 0 else -1)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
