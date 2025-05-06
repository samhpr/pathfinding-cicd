# define node classs being used
from constants import BLACK, WHITE, RED, YELLOW, BLUE, PURPLE, GREEN

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == YELLOW

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == BLUE

    def is_end(self):
        return self.color == PURPLE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = YELLOW

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = BLUE

    def make_end(self):
        self.color = PURPLE

    def make_path(self):
        self.color = GREEN

    def draw(self, win):
        # import pygame only when drawing, to decouple tests from pygame dependency
        import pygame
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        rows = self.total_rows
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                r, c = self.row + dr, self.col + dc
                if 0 <= r < rows and 0 <= c < rows and not grid[r][c].is_barrier():
                    self.neighbors.append(grid[r][c])

    def __lt__(self, other):
        return False