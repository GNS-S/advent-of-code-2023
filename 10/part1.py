import numpy as np
import numpy.typing as npt

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        maze = parse_input(f)
        start = tuple(np.argwhere(maze == 'S')[0])
        surrounds = surrounding(maze, start)
    
        start_conns = []
        for s in surrounds:
            conns = get_connections(s, maze[s])
            for c in conns:
                if c == start:
                    start_conns.append(s)
        
        previous = start
        current = start_conns[0]
        i = 0
        while current != start:
            nxt = forward(maze, previous, current)

            i += 1
            previous = current
            current = nxt

        print(int((i + 1) / 2))

def forward(maze: npt.NDArray, prev: tuple[int, int], curr: tuple[int, int]) -> tuple[int, int]:
    prev_x, prev_y = prev

    connections = get_connections(curr, maze[curr])
    for conn in connections:
        x, y = conn
        if x != prev_x or y != prev_y:
            return (x, y)

def get_connections(coords: tuple[int, int], symbol: str) -> list[tuple]:
    x, y = coords
    match symbol:
        case '|':
            return [(x - 1, y), (x + 1, y)]
        case '-':
            return [(x, y - 1), (x, y + 1)]
        case 'L':
            return [(x - 1, y), (x, y + 1)]
        case 'J':
            return [(x - 1, y), (x, y - 1)]
        case '7':
            return [(x + 1, y), (x, y - 1)]
        case 'F':
            return [(x + 1, y), (x, y + 1)]
        case _:
            return []

def surrounding(maze: npt.NDArray, coords: tuple[int, int]) -> list[tuple]:
    x, y = coords
    max_x, max_y = maze.shape
    surrounds = []

    for i in range(max(0, x - 1), min(max_x, x + 2)):
        for j in range(max(0, y - 1), min(max_y, y + 2)):
            if (i, j) != coords:
                surrounds.append((i, j))

    return surrounds

def parse_input(file) -> npt.NDArray:
    rows = []
    for line in file:
        cols = np.array(list(line.strip()))
        rows.append(cols)

    return np.array(rows)

if __name__ == '__main__':
    main()
