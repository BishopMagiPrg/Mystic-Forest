import pygame
import os

# Constants
WIDTH, HEIGHT = 800, 660
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame and window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mystic Forest")
font = pygame.font.SysFont("arial", 24)
clock = pygame.time.Clock()

# Load forest image
image_path = os.path.join("assets", "mystic_forest.jpg")
forest_image = pygame.image.load(image_path)
forest_image = pygame.transform.scale(forest_image, (WIDTH, 400))

def draw_scene(text_lines):
    screen.fill(WHITE)

    # Draw forest image
    screen.blit(forest_image, (0, 0))

    # Draw text box background
    pygame.draw.rect(screen, WHITE, (0, 400, WIDTH, 200))

    # Draw text
    y_offset = 410
    for line in text_lines:
        rendered = font.render(line, True, BLACK)
        screen.blit(rendered, (20, y_offset))
        y_offset += 30

def wait_for_keypress():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                return

def draw_button(text, x, y, width, height):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (200, 200, 200), rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    font = pygame.font.SysFont("arial", 24, bold=True)
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

    return rect

# This function will be used to update the display with buttons as well

def update_display(text_lines, button_data):
    draw_scene(text_lines)
    button_rects = []
    y_start = 250
    for i, (label, _) in enumerate(button_data):
        rect = draw_button(label, 100, y_start + i * 60, 600, 50)
        button_rects.append((rect, button_data[i]))
    pygame.display.flip()
    clock.tick(60)
    return button_rects
