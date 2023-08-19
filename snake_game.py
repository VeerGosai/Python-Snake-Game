import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake position and speed
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 15

# Food position
food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
            random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True

clock = pygame.time.Clock()

def draw_snake():
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

def draw_food():
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_LEFT]:
            snake_pos[0] -= 10
        if keys[pygame.K_RIGHT]:
            snake_pos[0] += 10
        if keys[pygame.K_UP]:
            snake_pos[1] -= 10
        if keys[pygame.K_DOWN]:
            snake_pos[1] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10,
                    random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawn = True

    screen.fill(BLACK)
    draw_snake()
    draw_food()

    if snake_pos[0] < 0 or snake_pos[0] > WIDTH - 10:
        pygame.quit()
        quit()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT - 10:
        pygame.quit()
        quit()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(snake_speed)
