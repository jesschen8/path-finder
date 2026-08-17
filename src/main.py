import pygame
from grid import make_grid, draw, get_clicked_position, ROWS

WIDTH = 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finder")

def main():
    grid = make_grid(ROWS, WIDTH)
    running = True

    while running:
        draw(screen, grid, ROWS, WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()