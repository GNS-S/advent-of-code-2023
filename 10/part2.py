from part1 import forward, get_connections, surrounding, parse_input

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

        x, y = start
        north_facing_pipes = ['|', 'J', 'L']
        north_facing_conns = [
            ((x - 1, y), (x + 1, y)),
            ((x - 1, y), (x, y - 1)),
            ((x - 1, y), (x, y + 1))
        ]

        for i, nfc in enumerate(north_facing_conns):
            if all(conn in nfc for conn in start_conns):
                maze[start] = north_facing_pipes[i]

        maze_pipes = [start]
        previous = start
        current = start_conns[0]
        while current != start:
            nxt = forward(maze, previous, current)

            maze_pipes.append(current)
            previous = current
            current = nxt

        tiles_inside = 0;
        for i in range(maze.shape[0]):
            maze_row = [pipe for pipe in maze_pipes if pipe[0] == i]
            for j in range(maze.shape[1]):
                if (i, j) in maze_row:
                    continue

                nf_left = [maze[pipe] for pipe in maze_row if (pipe[1] < j and maze[pipe] in north_facing_pipes)]
                if len(nf_left) % 2 == 1:
                    tiles_inside += 1

        print(tiles_inside)

if __name__ == '__main__':
    main()
