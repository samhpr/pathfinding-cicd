# tests/test_astar.py
import pytest
from astar import h, reconstruct_path, algorithm
from node import Node


def make_grid(rows):
    return [[Node(i, j, 1, rows) for j in range(rows)] for i in range(rows)]


def test_heuristic():
    assert h((0, 0), (3, 4)) == 7
    assert h((1, 2), (1, 2)) == 0


def test_reconstruct_path():
    class Dummy:
        def __init__(self, name): self.name = name
        def __repr__(self): return f"Dummy({self.name})"

    A, B, C = Dummy('A'), Dummy('B'), Dummy('C')
    came_from = { B: A, C: B }
    path = reconstruct_path(came_from, C)
    # Should reconstruct back through B to A
    assert path == [A, B]


def test_algorithm_no_path():
    grid = make_grid(2)
    start, end = grid[0][0], grid[1][1]
    # block all neighbors to end
    for neighbor in [(0,1), (1,0), (1,1)]:
        grid[neighbor[0]][neighbor[1]].make_barrier()
    for row in grid:
        for node in row:
            node.update_neighbors(grid)

    path = algorithm(grid, start, end)
    assert path == []


def test_algorithm_simple_path():
    grid = make_grid(2)
    start, end = grid[0][0], grid[1][1]
    for row in grid:
        for node in row:
            node.update_neighbors(grid)

    path = algorithm(grid, start, end)
    # Diagonal adjacency yields a single-step path (start -> end)
    assert path == [start]


def test_algorithm_start_equals_end():
    grid = make_grid(1)
    start = end = grid[0][0]
    start.update_neighbors(grid)
    path = algorithm(grid, start, end)
    assert path == []


def test_algorithm_longer_path():
    grid = make_grid(3)
    start, end = grid[0][0], grid[2][2]
    for row in grid:
        for node in row:
            node.update_neighbors(grid)
    path = algorithm(grid, start, end)
    # Path should step through the midpoint (1,1)
    assert path == [start, grid[1][1]]
