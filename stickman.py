import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stickman Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Stickman position
x, y = 100, 300
dx = 2
wave = False  # Hand waving flag

# Font for text
font = pygame.font.Font(None, 40)

def draw_stickman(screen, x, y, wave):
    # Head
    pygame.draw.circle(screen, BLACK, (x, y - 60), 20, 2)
    # Body
    pygame.draw.line(screen, BLACK, (x, y - 40), (x, y + 40), 2)
    # Arms
    if wave:  # Waving hand
        pygame.draw.line(screen, BLACK, (x, y - 20), (x + 20, y - 50), 2)
    else:  # Normal arms
        pygame.draw.line(screen, BLACK, (x, y - 20), (x + 40, y - 30), 2)
    pygame.draw.line(screen, BLACK, (x, y - 20), (x - 40, y - 30), 2)
    # Legs
    pygame.draw.line(screen, BLACK, (x, y + 40), (x + 20, y + 80), 2)
    pygame.draw.line(screen, BLACK, (x, y + 40), (x - 20, y + 80), 2)

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update stickman position
    x += dx
    if x > WIDTH - 100 or x < 100:
        dx = -dx  # Reverse direction

    # Trigger waving when moving left
    wave = dx < 0

    # Draw stickman and text
    draw_stickman(screen, x, y, wave)
    text = font.render("Hi!", True, BLACK)
    if wave:
        screen.blit(text, (x + 25, y - 80))

    pygame.display.flip()
    clock.tick(30)

# Quit pygame
pygame.quit()
sys.exit()