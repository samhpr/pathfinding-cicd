# astar.py
# Core A* algorithm and heuristics extracted for testability
from queue import PriorityQueue


def h(p1, p2):
    """
    Heuristic function: Manhattan distance between two points p1 and p2.
    p1, p2: tuples (row, col)
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, end):
    """
    Reconstructs the path from start to end given a map of navigations.
    Returns a list of nodes from start (excluded) to end (included).
    """
    path = []
    current = end
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def algorithm(grid, start, end):
    """
    Runs the A* algorithm on a grid of Node objects.
    Each Node must have:
      - get_pos() -> (row, col)
      - neighbors: list of adjacent Node objects
    Returns:
      - path: list of Nodes from start (excluded) to end (included), or [] if no path found
    """
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    # g_score: cost from start to this node
    g_score = {node: float('inf') for row in grid for node in row}
    g_score[start] = 0

    # f_score: estimated total cost (g + h)
    f_score = {node: float('inf') for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        _, _, current = open_set.get()
        open_set_hash.remove(current)

        if current == end:
            return reconstruct_path(came_from, end)

        for neighbor in current.neighbors:
            tentative_g = g_score[current] + 1
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)

    # no path found
    return []
