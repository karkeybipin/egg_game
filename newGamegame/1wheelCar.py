import pygame
import math

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Car and Wheels")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
car_image = pygame.image.load('car.png')  
wheel_image = pygame.image.load('wheel.png')  
wheel_image = pygame.transform.scale(wheel_image, (50, 50))


def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)


car_x = 200
car_y = 300
front_wheel_pos = (car_x + 60, car_y + 80)
back_wheel_pos = (car_x - 20, car_y + 80)
angle = 0
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    angle -= 5
    screen.blit(car_image, (car_x, car_y))
    rotated_wheel_front = rotate_image(wheel_image, angle)
    rotated_wheel_back = rotate_image(wheel_image, angle)
    front_wheel_rect = rotated_wheel_front.get_rect(center=front_wheel_pos)
    back_wheel_rect = rotated_wheel_back.get_rect(center=back_wheel_pos)
    screen.blit(rotated_wheel_front, front_wheel_rect)
    screen.blit(rotated_wheel_back, back_wheel_rect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Car and Wheels")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
# image
car_image = pygame.image.load('car.png')  
wheel_image = pygame.image.load('wheel.png')  
wheel_image = pygame.transform.scale(wheel_image, (50, 50))

