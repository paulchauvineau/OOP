import pygame
import math

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 640
screen_height = 480

# Set the player size
player_size = 50

# Set the ball properties
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_radius = 10
ball_speed = 0
ball_max_speed = 10
ball_direction = math.pi / 4
ball_bounce_force = 2
ball_slowdown_factor = 0.99

# Set the colors
background_color = (255, 255, 255)
ball_color = (255, 0, 0)
player1_color = (0, 0, 255)
player2_color = (0, 255, 0)

# Set the player positions
player1_x = 20
player1_y = screen_height / 2 - player_size / 2
player2_x = screen_width - player_size - 20
player2_y = screen_height / 2 - player_size / 2

# Set the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the clock
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= 5
    if keys[pygame.K_s]:
        player1_y += 5
    if keys[pygame.K_a]:
        player1_x -= 5
    if keys[pygame.K_d]:
        player1_x += 5
    if keys[pygame.K_UP]:
        player2_y -= 5
    if keys[pygame.K_DOWN]:
        player2_y += 5
    if keys[pygame.K_LEFT]:
        player2_x -= 5
    if keys[pygame.K_RIGHT]:
        player2_x += 5

    # Move the ball
    ball_x += ball_speed * math.cos(ball_direction)
    ball_y += ball_speed * math.sin(ball_direction)

    # Bounce off the walls
    if ball_x < ball_radius or ball_x > screen_width - ball_radius:
        ball_direction = math.pi - ball_direction
        ball_speed += ball_bounce_force
        ball_speed = min(ball_speed, ball_max_speed)
        ball_speed *= ball_slowdown_factor
    if ball_y < ball_radius or ball_y > screen_height - ball_radius:
        ball_direction = -ball_direction
        ball_speed += ball_bounce_force
        ball_speed = min(ball_speed, ball_max_speed)
        ball_speed *= ball_slowdown_factor

    # Bounce off the players
    player1_rect = pygame.Rect(player1_x, player1_y, player_size, player_size)
    player2_rect = pygame.Rect(player2_x, player2_y, player_size, player_size)
    if player1_rect.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
        ball_direction = math.pi - ball_direction
        ball_speed += ball_bounce_force
        ball_direction += (player1_x + player_size // 2 - ball_x) / (player_size // 2) * math.pi / 4
        ball_import
import math

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 640
screen_height = 480

# Set the player size
player_size = 50

# Set the ball properties
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_radius = 10
ball_speed = 0
ball_max_speed = 10
ball_direction = math.pi / 4
ball_bounce_force = 2
ball_slowdown_factor = 0.99

# Set the colors
background_color = (255, 255, 255)
ball_color = (255, 0, 0)
player1_color = (0, 0, 255)
player2_color = (0, 255, 0)

# Set the player positions
player1_x = 20
player1_y = screen_height / 2 - player_size / 2
player2_x = screen_width - player_size - 20
player2_y = screen_height / 2 - player_size / 2

# Set the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the clock
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= 5
    if keys[pygame.K_s]:
        player1_y += 5
    if keys[pygame.K_a]:
        player1_x -= 5
    if keys[pygame.K_d]:
        player1_x += 5
    if keys[pygame.K_UP]:
        player2_y -= 5
    if keys[pygame.K_DOWN]:
        player2_y += 5
    if keys[pygame.K_LEFT]:
        player2_x -= 5
    if keys[pygame.K_RIGHT]:
        player2_x += 5

    # Move the ball
    ball_x += ball_speed * math.cos(ball_direction)
    ball_y += ball_speed * math.sin(ball_direction)

    # Bounce off the walls
    if ball_x < ball_radius or ball_x > screen_width - ball_radius:
        ball_direction = math.pi - ball_direction
        ball_speed += ball_bounce_force
        ball_speed = min(ball_speed, ball_max_speed)
        ball_speed *= ball_slowdown_factor
    if ball_y < ball_radius or ball_y > screen_height - ball_radius:
        ball_direction = -ball_direction
        ball_speed += ball_bounce_force
        ball_speed = min(ball_speed, ball_max_speed)
        ball_speed *= ball_slowdown_factor

    # Bounce off the players
    player1_rect = pygame.Rect(player1_x, player1_y, player_size, player_size)
    player2_rect = pygame.Rect(player2_x, player2_y, player_size, player_size)
    if player1_rect.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
        ball_direction = math.pi - ball_direction
        ball_speed += ball_bounce_force
        ball_direction += (player1_x + player_size // 2 - ball_x) / (player_size // 2) * math.pi / 4
        ball_speed = min(ball_speed, ball_max_speed)
        ball_speed *= ball
    if player2_rect.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
        ball_direction = math.pi - ball_direction
        ball_speed += ball_bounce_force
        ball_direction += (player2_x + player_size // 2 - ball_x) / (player_size // 2) * math.pi / 4
        ball_speed = min(ball_speed, ball_max_speed)
        ball_speed *= ball_slowdown_factor

    # Slow down the ball
    if ball_speed > 0.01:
        ball_speed *= ball_slowdown_factor
    else:
        ball_speed = 0

    # Draw the screen
    screen.fill(background_color)
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)
    pygame.draw.rect(screen, player1_color, (player1_x, player1_y, player_size, player_size))
    pygame.draw.rect(screen, player2_color, (player2_x, player2_y, player_size, player_size))
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
d = min(ball_speed, ball_max_speed)
        ball_speed *= ball
    if player2_rect.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
        ball_direction = math.pi - ball_direction
        ball_speed += ball_bounce_force
        ball_direction += (player2_x + player_size // 2 - ball_x) / (player_size // 2) * math.pi / 4
        ball_speed = min(ball_speed, ball_max_speed)
        ball_speed *= ball_slowdown_factor

    # Slow down the ball
    if ball_speed > 0.01:
        ball_speed *= ball_slowdown_factor
    else:
        ball_speed = 0

    # Draw the screen
    screen.fill(background_color)
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)
    pygame.draw.rect(screen, player1_color, (player1_x, player1_y, player_size, player_size))
    pygame.draw.rect(screen, player2_color, (player2_x, player2_y, player_size, player_size))
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
