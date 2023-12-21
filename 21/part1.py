from collections import deque

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid, start = parse_input(f)

        print(count_stops(grid, start, 64))

def count_stops(grid: list, start: tuple, stop_at: int, loop_grid=False) -> int:
    assert len(grid) == len(grid[0])

    size = len(grid)
    stops = set()
    VISITED = {}
    Q = deque([(start, 0)])

    while Q:
        position, step = Q.popleft()
        r, c = position

        if position in VISITED and VISITED[position] >= step:
            continue

        VISITED[position] = step

        if step == stop_at:
            stops.add(position)
            continue

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = r + dr
            new_c = c + dc
            
            if loop_grid and grid[new_r % size][new_c % size] != '#':
                Q.append(((new_r, new_c), step + 1))

            elif 0 <= new_r < size and 0 <= new_c < size and grid[new_r][new_c] != '#':
                Q.append(((new_r, new_c), step + 1))
    
    return len(stops)

def parse_input(file) -> tuple[list, tuple]:
    grid = []
    start_marker = 'S'

    for r, line in enumerate(file):
        row = list(line.strip())
        if start_marker in row:
            start = (r, row.index(start_marker))

        grid.append(row)

    return grid, start

if __name__ == '__main__':
    main()
