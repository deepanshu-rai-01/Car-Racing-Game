import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player Car
car_width = 50
car_height = 90
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - 120
car_speed = 6

# Enemy Car
enemy_width = 50
enemy_height = 90
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont("Arial", 30)

running = True

while running:
    clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed

    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Move Enemy
    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)
        score += 1
        enemy_speed += 0.2

    # Collision Detection
    player_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        print("Final Score:", score)
        running = False

    # Background
    screen.fill(GRAY)

    # Road Lines
    for y in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 5, y, 10, 20))

    # Draw Cars
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    # Score Display
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
