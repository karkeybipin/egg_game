import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lane Dodger")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60
clock = pygame.time.Clock()
CAR_WIDTH, CAR_HEIGHT = 50, 90
LANES = [60, 175, 290]  # 3 lanes (left, middle, right)
car_img = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_img.fill(BLUE)
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 90
font = pygame.font.Font(None, 50)
def display_message(text):
    """Displays a message in the center of the screen."""
    message = font.render(text, True, WHITE)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(2000)
def main():
    car_x = LANES[1]
    car_y = HEIGHT - CAR_HEIGHT - 10
    car_lane = 1
    obstacles = []
    score = 0

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and car_lane > 0:
                    car_lane -= 1
                if event.key == pygame.K_RIGHT and car_lane < 2:
                    car_lane += 1
        car_x = LANES[car_lane]
        screen.blit(car_img, (car_x, car_y))
        if random.randint(1, 50) == 1:
            obstacle_lane = random.randint(0, 2)
            obstacles.append([LANES[obstacle_lane], -OBSTACLE_HEIGHT])
        for obstacle in obstacles:
            obstacle[1] += 5
        obstacles = [obstacle for obstacle in obstacles if obstacle[1] < HEIGHT]
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
        for obstacle in obstacles:
            obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
            if car_rect.colliderect(obstacle_rect):
                display_message("Game Over")
                running = False
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.update()
        score += 1
    pygame.quit()
if __name__ == "__main__":
    main()
