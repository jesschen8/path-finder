from queue import PriorityQueue

def h(node_a, node_b):                      #heuristic function using manhattan distance for 4 direction movement
    row_a, col_a = node_a.get_position()
    row_b, col_b = node_b.get_position()
    return abs(row_a - row_b) + abs(col_a - col_b)

def trace_path(came_from, end, start):
    current = came_from[end]
    while current is not start:
        current.state = "path"
        current = came_from[current]
        yield
