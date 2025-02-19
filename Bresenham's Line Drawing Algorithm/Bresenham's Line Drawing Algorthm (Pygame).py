import pygame

def bresenham_line(x1, y1, x2, y2):
    """Implements Bresenham's Line Algorithm to generate points for a line."""
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    return points

# Initialize pygame
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bresenham's Kite - Pygame")

# Kite edges (scaled for pygame screen)
kite_edges = [
    ((250, 100), (150, 250)),  # Top to left
    ((150, 250), (250, 350)),  # Left to bottom
    ((250, 350), (350, 250)),  # Bottom to right
    ((350, 250), (250, 100))   # Right to top
]

cross_lines = [
    ((150, 250), (350, 250)),  # Horizontal cross
    ((250, 100), (250, 350))   # Vertical cross
]

tail_edges = [
    ((250, 350), (200, 450)),  # Top to bottom-left
    ((200, 450), (300, 450)),  # Bottom-left to bottom-right
    ((300, 450), (250, 350))   # Bottom-right to top
]

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    for line in kite_edges + cross_lines + tail_edges:
        x1, y1 = line[0]
        x2, y2 = line[1]
        points = bresenham_line(x1, y1, x2, y2)
        for px, py in points:
            screen.set_at((px, py), (255, 0, 0))  # Draw pixel in red

    pygame.display.flip()  # Update display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
