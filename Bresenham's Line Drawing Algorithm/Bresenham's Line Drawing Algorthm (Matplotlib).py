import matplotlib.pyplot as plt

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

# Kite edges
kite_edges = [
    ((0, 2), (-1, 0)),  # Top to left
    ((-1, 0), (0, -1.5)),  # Left to bottom
    ((0, -1.5), (1, 0)),  # Bottom to right
    ((1, 0), (0, 2))  # Right to top
]

# Cross lines inside the kite
cross_lines = [
    ((-1, 0), (1, 0)),  # Horizontal cross
    ((0, 2), (0, -1.5))  # Vertical cross
]

# Triangular Tail
tail_edges = [
    ((0, -1.5), (-0.5, -2.5)),  # Top to bottom-left
    ((-0.5, -2.5), (0.5, -2.5)),  # Bottom-left to bottom-right
    ((0.5, -2.5), (0, -1.5))  # Bottom-right to top
]

# Plot setup
plt.figure(figsize=(6, 6))
for line in kite_edges + cross_lines + tail_edges:
    x1, y1 = line[0]
    x2, y2 = line[1]
    points = bresenham_line(int(x1 * 100), int(y1 * 100), int(x2 * 100), int(y2 * 100))
    x_vals, y_vals = zip(*points)
    plt.plot([x / 100 for x in x_vals], [y / 100 for y in y_vals], 'r-', linewidth=1)

# Display settings
plt.xlim(-2, 2)
plt.ylim(-3, 3)
plt.gca().set_aspect('equal')
plt.title("Kite with Bresenham's Line Algorithm - Matplotlib")
plt.grid()
plt.show()
