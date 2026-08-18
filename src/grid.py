import pygame

STATES = {
    "empty" : (255, 255, 255),
    "wall" : (0,0,0),
    "start" : (173, 246, 249),
    "end" : (58, 58, 210),
    "path" : (150, 253, 157),
    "open" : (0, 255, 0),
    "closed": (255, 0, 0),
}

LINE_COLOUR = (203, 203, 205)
ROWS = 50

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.x = col * width
        self.y = row * width
        self.state = "empty"
        self.neighbours = []

    def get_position(self):
        return self.row, self.col # returning a tuple (self.row, self.col)

    def draw(self, screen):
        pygame.draw.rect(screen, STATES[self.state], (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []  # refresh neighbours before each search run in case the walls are changed
        for delta_row, delta_col in ((-1, 0), (1,0), (0, -1), (0, 1)):
            r, c = self.row + delta_row, self.col + delta_col  # r, c are temp neigbhouring values
            if not ((0 <= r < len(grid)) and (0 <= c < len(grid[0]))):
                continue
            if grid[r][c].state == "wall":
                continue
            self.neighbours.append(grid[r][c])


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        row = []
        for j in range(rows):
            row.append(Node(i, j, gap))
        grid.append(row)
    return grid

def draw_lines(screen, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(screen, LINE_COLOUR, (0, i * gap), (width, i * gap))
        pygame.draw.line(screen, LINE_COLOUR, ( i * gap, 0), (i * gap, width))

def draw(screen, grid, rows, width):
    screen.fill(STATES["empty"])
    for row in grid:
        for node in row:
            node.draw(screen)
    draw_lines(screen, rows, width)
    pygame.display.update()

def get_clicked_position(pos, rows, width):
    gap = width // rows
    x, y = pos
    return y // gap, x // gap #return (row, col)

