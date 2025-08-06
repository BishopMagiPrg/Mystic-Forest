import pygame
import os

# Constants
WIDTH, HEIGHT = 800, 660
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame and window
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mystic Forest")
font = pygame.font.SysFont("arial", 24)

# Load forest image
image_path = os.path.join("assets", "mystic_forest.jpg")
forest_image = pygame.image.load(image_path)
forest_image = pygame.transform.scale(forest_image, (WIDTH, 400))

def draw_scene(text_lines):
    window.fill(WHITE)

    # Draw forest image
    window.blit(forest_image, (0, 0))

    # Draw text box background
    pygame.draw.rect(window, WHITE, (0, 400, WIDTH, 200))

    # Draw text
    y_offset = 410
    for line in text_lines:
        rendered = font.render(line, True, BLACK)
        window.blit(rendered, (20, y_offset))
        y_offset += 30

    pygame.display.update()

def wait_for_keypress():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                return
