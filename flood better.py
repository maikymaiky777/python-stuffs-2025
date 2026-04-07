import heapq

# ─── CONFIGURE YOUR MAZE HERE ───────────────────────────────────────────────
# Use numbers for movement cost, "S" for start, "E" for end, None for walls
MAZE = [
    ["S",1,7,10,9],
    [5,4,3,5,1],
    [2,7,0,4,2],
    [0,1,8,3,"E"],

]
# ────────────────────────────────────────────────────────────────────────────

def parse_grid(maze):
    sy = len(maze)
    sx = len(maze[0])
    grid = []
    start = end = None

    for row_idx, row in enumerate(maze):
        grid_row = []
        for col_idx, cell in enumerate(row):
            if cell == "S":
                start = (col_idx, row_idx)
                grid_row.append(0)
            elif cell == "E":
                end = (col_idx, row_idx)
                grid_row.append(0)
            elif cell is None:
                grid_row.append(None)
            else:
                grid_row.append(int(cell))
        grid.append(grid_row)

    assert start is not None, "No 'S' found in maze"
    assert end is not None,   "No 'E' found in maze"
    return grid, sx, sy, start, end


def dijkstra(grid, sx, sy, start, end):
    INF = float("inf")
    dist = [[INF] * sx for _ in range(sy)]
    prev = [[None] * sx for _ in range(sy)]  # track previous node for path reconstruction
    x0, y0 = start
    dist[y0][x0] = 0

    heap = [(0, start)]

    while heap:
        cost, (x, y) = heapq.heappop(heap)

        if (x, y) == end:
            break

        if cost > dist[y][x]:
            continue

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < sx and 0 <= ny < sy:
                cell = grid[ny][nx]
                if cell is not None:
                    new_cost = cost + cell
                    if new_cost < dist[ny][nx]:
                        dist[ny][nx] = new_cost
                        prev[ny][nx] = (x, y)  # record where we came from
                        heapq.heappush(heap, (new_cost, (nx, ny)))

    # reconstruct path by walking backwards from end via prev
    path = []
    node = end
    while node is not None:
        path.append(node)
        x, y = node
        node = prev[y][x]
    path.reverse()

    # if path doesn't start at start, no path exists
    if path[0] != start:
        return dist[end[1]][end[0]], dist, []

    return dist[end[1]][end[0]], dist, path


def print_maze_with_path(maze, path, start, end):
    path_set = set(path)
    sy = len(maze)
    sx = len(maze[0])

    # build step number lookup: (x,y) -> step index
    step_num = {pos: i for i, pos in enumerate(path)}

    print("\nPath visualized ('·' = path, '█' = wall):\n")

    # column index header
    print("     " + "  ".join(f"{c}" for c in range(sx)))
    print("    +" + "---" * sx + "+")

    for row_idx in range(sy):
        row_str = f" {row_idx}  |"
        for col_idx in range(sx):
            pos = (col_idx, row_idx)
            cell = maze[row_idx][col_idx]
            if pos == start:
                row_str += " S "
            elif pos == end:
                row_str += " E "
            elif cell is None:
                row_str += " █ "
            elif pos in path_set:
                row_str += " · "
            else:
                row_str += f" {cell} "
        row_str += "|"
        print(row_str)

    print("    +" + "---" * sx + "+")


def print_path_steps(path, grid, maze):
    print("\nStep-by-step path:")
    total = 0
    for i, (x, y) in enumerate(path):
        cell = maze[y][x]
        if cell == "S":
            label = "S (start, cost 0)"
            cost = 0
        elif cell == "E":
            label = "E (end,  cost 0)"
            cost = 0
        else:
            cost = grid[y][x]
            label = f"cost {cost}"
        total += cost
        print(f"  Step {i:>2}: ({x}, {y})  →  {label}   [running total: {total}]")


grid, sx, sy, start, end = parse_grid(MAZE)
min_cost, dist, path = dijkstra(grid, sx, sy, start, end)

if not path:
    print("No path found from S to E!")
else:
    print_maze_with_path(MAZE, path, start, end)
    print_path_steps(path, grid, MAZE)
    print(f"\nMinimum energy: {min_cost}")
