import pytest
from node import Node
from constants import BLACK

def make_grid(rows):
    return [[Node(i, j, 1, rows) for j in range(rows)] for i in range(rows)]

def test_neighbors_center():
    grid = make_grid(3)
    center = grid[1][1]
    for row in grid:
        for node in row:
            node.reset()
    center.update_neighbors(grid)
    assert len(center.neighbors) == 8  # all around

def test_neighbors_corner():
    grid = make_grid(3)
    corner = grid[0][0]
    corner.update_neighbors(grid)
    # only (0,1), (1,0), (1,1)
    expected = {grid[0][1], grid[1][0], grid[1][1]}
    assert set(corner.neighbors) == expected

def test_neighbors_edge():
    grid = make_grid(3)
    edge = grid[0][1]
    edge.update_neighbors(grid)
    # should have 5 neighbors
    assert len(edge.neighbors) == 5

def test_neighbors_barrier():
    grid = make_grid(3)
    # block one diagonal neighbor of center
    grid[2][2].make_barrier()
    center = grid[1][1]
    center.update_neighbors(grid)
    # originally 8, minus 1 barrier = 7
    assert len(center.neighbors) == 7

def test_node_lt_always_false():
    a = Node(0,0,1,1)
    b = Node(0,1,1,1)
    assert (a < b) is False
