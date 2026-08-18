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

def astar(grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    open_set_v2 = {start}
    came_from = {}

    g_score = {}
    for row in grid:
        for node in row:
            g_score[node] = float("inf")
    g_score[start] = 0

    f_score = {}
    for row in grid:
        for node in row:
            f_score[node] = float("inf")
    f_score[start] = h(start, end)

    while not open_set.empty():
        current_node = open_set.get()[2]
        open_set_v2.remove(current_node)

        if current_node is end:
            yield from trace_path(came_from, end, start)
            start.state = "start"
            end.state = "end"
            return True

        for neighbour in current_node.neighbours:
            temp_g = g_score[current_node] + 1

            if temp_g < g_score[neighbour]:
                came_from[neighbour] = current_node
                g_score[neighbour] = temp_g
                f_score[neighbour] = temp_g + h(neighbour, end)

                if neighbour not in open_set_v2:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_v2.add(neighbour)
                    if neighbour is not end:
                        neighbour.state = "open"

        if current_node is not start:
            current_node.state = "closed"

        yield
    return False