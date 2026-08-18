import pygame
from grid import make_grid, draw, get_clicked_position, ROWS

WIDTH = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finder")

def main():
    grid = make_grid(ROWS, WIDTH)
    running = True
    start = None
    end = None

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

            if event.type == pygame.KEYDOWN:  #clear grid
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, WIDTH)

    pygame.quit()

if __name__ == "__main__":
    main()