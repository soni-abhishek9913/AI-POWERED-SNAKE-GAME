import pygame
import random

pygame.init()

# Window size
WIDTH, HEIGHT = 400, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - User Controlled")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initial snake
snake = [(100, 100)]
direction = (CELL, 0)  # Start moving right

# Food
food = (random.randrange(0, WIDTH, CELL),
        random.randrange(0, HEIGHT, CELL))

running = True
while running:
    screen.fill(BLACK)

    # 🎮 Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # ❌ Collision with wall or self
    if (new_head in snake or
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        print("Game Over")
        running = False

    snake.insert(0, new_head)

    # 🍎 Eat food
    if new_head == food:
        food = (random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL))
    else:
        snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
