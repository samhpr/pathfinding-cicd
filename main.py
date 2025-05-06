# main.py
# Pygame UI for A* pathfinding visualization, uses core logic from astar.py

import pygame
from astar import algorithm
from node import Node  # assume Node class moved to node.py for clarity
from constants import BLACK, WHITE, RED, YELLOW, BLUE, PURPLE, GREEN

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
PURPLE = (138, 43, 226)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRAY, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, GRAY, (i * gap, 0), (i * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col


def main(win, width):
    ROWS = 50
    grid = [[Node(i, j, width // ROWS, ROWS) for j in range(ROWS)] for i in range(ROWS)]
    start = end = None
    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # left click
                row, col = get_clicked_pos(pygame.mouse.get_pos(), ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node not in (start, end):
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # right click
                row, col = get_clicked_pos(pygame.mouse.get_pos(), ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                if node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)

                    path = algorithm(grid, start, end)
                    for node in path:
                        node.make_path()
                    end.make_end()
                    start.make_start()

                if event.key == pygame.K_c:
                    start = end = None
                    grid = [[Node(i, j, width // ROWS, ROWS) for j in range(ROWS)] for i in range(ROWS)]

    pygame.quit()


if __name__ == "__main__":
    main(WIN, WIDTH)
