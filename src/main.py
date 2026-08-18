import pygame
from grid import make_grid, draw, get_clicked_position, ROWS
from algorithms import astar

WIDTH = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finder")

def main():
    grid = make_grid(ROWS, WIDTH)
    running = True
    start = None
    end = None
    search = None

    while running:
        draw(screen, grid, ROWS, WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:
                row, col = get_clicked_position(pygame.mouse.get_pos(), ROWS, WIDTH)
                node = grid[row][col]

                if start is None and node is not end:
                    start = node
                    node.state = "start"

                elif end is None and node is not start:
                    end = node
                    node.state = "end"

                elif node is not start and node is not end:
                    node.state = "wall"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)
                    search = astar(grid, start, end)

                if event.key == pygame.K_c: #clear grid
                    start = None
                    end = None
                    search = None
                    grid = make_grid(ROWS, WIDTH)

        if search is not None:
            try:
                next(search)
            except StopIteration as e:
                if e.value is False:
                    print("No path found")
                search = None

    pygame.quit()

if __name__ == "__main__":
    main()