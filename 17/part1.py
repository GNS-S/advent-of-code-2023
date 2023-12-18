from collections import defaultdict
from collections.abc import Callable
from heapq import heappop, heappush
from math import inf

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)

        def criteria(current: tuple, new: tuple):
            _, _, _, direction, _ = current
            _, _, _, new_direction, new_lin_steps = new

            step_limit_ok = new_lin_steps <= 3
            is_reverse = (new_direction + 2) % 4 == direction

            return step_limit_ok and not is_reverse
        
        dists = dijkstra(grid,criteria)

        target = len(grid) - 1, len(grid[0]) - 1
        shortest = inf
        for key in dists:
            r, c, _, _ = key
            if (r, c) == target:
                shortest = min(shortest, dists[key])

        print(shortest)

def dijkstra(graph: list[list[int]], criteria: Callable[[tuple], bool]) -> dict[tuple, int]:
    max_r, max_c = len(graph), len(graph[0])

    # distance, row, column, direction (index[up, right, down, left]), linear steps
    root = (0, 0, 0, -1, -1)
    PQ = [root]
    DIST = defaultdict(lambda: inf)

    while PQ:
        current = heappop(PQ)
        distance, r, c, direction, lin_steps = current
        
        key = (r, c, direction, lin_steps)
        if key in DIST:
            continue
        DIST[key] = distance
        
        for i, (dr, dc) in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]):
            new_r = r + dr
            new_c = c + dc
            new_direction = i
            new_lin_steps = (lin_steps + 1 if new_direction == direction else 1)

            if 0 <= new_r < max_r and 0 <= new_c < max_c:
                new = (distance + graph[new_r][new_c], new_r, new_c, new_direction, new_lin_steps)

                if criteria(current, new):
                    heappush(PQ, new)
   
    return DIST

def parse_input(file) -> list[list[int]]:
    grid = []
    for line in file:
        grid.append([int(c) for c in list(line.strip())])

    return grid

if __name__ == '__main__':
    main()
