import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple 2D Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 10

# Obstacle settings
obstacle_size = 50
obstacle_pos = [random.randint(0, SCREEN_WIDTH - obstacle_size), 0]
obstacle_speed = 10

# Game variables
game_over = False
score = 0

# Font for displaying the score
font = pygame.font.SysFont("monospace", 35)


def draw_player(player_pos):
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))


def draw_obstacle(obstacle_pos):
    pygame.draw.rect(screen, BLACK, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))


def detect_collision(player_pos, obstacle_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    o_x = obstacle_pos[0]
    o_y = obstacle_pos[1]

    if (o_x >= p_x and o_x < (p_x + player_size)) or (p_x >= o_x and p_x < (o_x + obstacle_size)):
        if (o_y >= p_y and o_y < (p_y + player_size)) or (p_y >= o_y and p_y < (o_y + obstacle_size)):
            return True
    return False


# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += player_speed

    screen.fill(WHITE)

    draw_player(player_pos)
    draw_obstacle(obstacle_pos)

    obstacle_pos[1] += obstacle_speed
    if obstacle_pos[1] > SCREEN_HEIGHT:
        obstacle_pos[0] = random.randint(0, SCREEN_WIDTH - obstacle_size)
        obstacle_pos[1] = 0
        score += 1

    if detect_collision(player_pos, obstacle_pos):
        game_over = True

    score_text = font.render("Score: {}".format(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
