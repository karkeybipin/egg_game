import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lane Dodger")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Car settings
CAR_WIDTH, CAR_HEIGHT = 50, 90
LANES = [60, 175, 290]  # 3 lanes (left, middle, right)

# Load car image
car_img = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_img.fill(BLUE)

# Obstacle settings
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 90

# Fonts
font = pygame.font.Font(None, 50)

def display_message(text):
    """Displays a message in the center of the screen."""
    message = font.render(text, True, WHITE)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - message.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(2000)

def main():
    # Car starting position (middle lane)
    car_x = LANES[1]
    car_y = HEIGHT - CAR_HEIGHT - 10
    car_lane = 1

    # Obstacle list
    obstacles = []

    # Score
    score = 0

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Move car left or right with arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and car_lane > 0:
                    car_lane -= 1
                if event.key == pygame.K_RIGHT and car_lane < 2:
                    car_lane += 1

        # Update car position based on lane
        car_x = LANES[car_lane]

        # Draw car
        screen.blit(car_img, (car_x, car_y))

        # Add obstacles
        if random.randint(1, 50) == 1:
            obstacle_lane = random.randint(0, 2)
            obstacles.append([LANES[obstacle_lane], -OBSTACLE_HEIGHT])

        # Move obstacles down the screen
        for obstacle in obstacles:
            obstacle[1] += 5

        # Remove obstacles that are off the screen
        obstacles = [obstacle for obstacle in obstacles if obstacle[1] < HEIGHT]

        # Draw obstacles
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        # Check for collisions
        car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
        for obstacle in obstacles:
            obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
            if car_rect.colliderect(obstacle_rect):
                display_message("Game Over")
                running = False

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Increment score
        score += 1

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
