import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('My First Game')

# Colors
BLUE = (0, 128, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
new = (250, 255, 250)

# Player settings
player_size = 50
player_pos = [375, 525]
player_speed = 0.5

# Enemy settings
enemy_size = 50
enemy_pos = [375, 0]
enemy_speed = 0.02  # Adjust the speed so it's not too fast
enemy_direction = "down"  # Initial direction

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < 800 - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < 600 - player_size:
        player_pos[1] += player_speed

    # Move enemy towards player
    if enemy_pos[0] < player_pos[0]:
        enemy_pos[0] += enemy_speed
        enemy_direction = "right"
    elif enemy_pos[0] > player_pos[0]:
        enemy_pos[0] -= enemy_speed
        enemy_direction = "left"

    if enemy_pos[1] < player_pos[1]:
        enemy_pos[1] += enemy_speed
        enemy_direction = "down"
    elif enemy_pos[1] > player_pos[1]:
        enemy_pos[1] -= enemy_speed
        enemy_direction = "up"

    # Collision detection
    if (player_pos[0] < enemy_pos[0] < player_pos[0] + player_size or
        player_pos[0] < enemy_pos[0] + enemy_size < player_pos[0] + player_size) and \
       (player_pos[1] < enemy_pos[1] < player_pos[1] + player_size or
        player_pos[1] < enemy_pos[1] + enemy_size < player_pos[1] + player_size):
        print("Collision Detected!")
        pygame.quit()
        sys.exit()

    # Fill screen with color
    screen.fill(BLUE)

    # Draw player
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw enemy based on direction
    if enemy_direction == "left":
        pygame.draw.polygon(screen, RED, [(enemy_pos[0] + enemy_size, enemy_pos[1] + enemy_size / 2),
                                          (enemy_pos[0], enemy_pos[1]), 
                                          (enemy_pos[0], enemy_pos[1] + enemy_size)])
    elif enemy_direction == "right":
        pygame.draw.polygon(screen, RED, [(enemy_pos[0], enemy_pos[1] + enemy_size / 2),
                                          (enemy_pos[0] + enemy_size, enemy_pos[1]), 
                                          (enemy_pos[0] + enemy_size, enemy_pos[1] + enemy_size)])
    elif enemy_direction == "up":
        pygame.draw.polygon(screen, RED, [(enemy_pos[0], enemy_pos[1] + enemy_size),
                                          (enemy_pos[0] + enemy_size / 2, enemy_pos[1]), 
                                          (enemy_pos[0] + enemy_size, enemy_pos[1] + enemy_size)])
    elif enemy_direction == "down":
        pygame.draw.polygon(screen, RED, [(enemy_pos[0], enemy_pos[1]), 
                                          (enemy_pos[0] + enemy_size / 2, enemy_pos[1] + enemy_size), 
                                          (enemy_pos[0] + enemy_size, enemy_pos[1])])

    # Update display
    pygame.display.flip()
