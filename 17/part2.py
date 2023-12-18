from part1 import parse_input, dijkstra

from collections import defaultdict
from collections.abc import Callable
from heapq import heappop, heappush
from math import inf

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)

        def criteria(current: tuple, new: tuple):
            _, _, _, direction, lin_steps = current
            _, _, _, new_direction, new_lin_steps = new

            no_steps_yet = lin_steps == -1
            same_direction = direction == new_direction
            step_limit_ok = new_lin_steps <= 10 and (lin_steps >= 4 or no_steps_yet or same_direction)
            is_reverse = (new_direction + 2) % 4 == direction

            return step_limit_ok and not is_reverse

        dists = dijkstra(grid,criteria)

        target = len(grid) - 1, len(grid[0]) - 1
        shortest = inf
        for key in dists:
            r, c, _, lin_steps = key
            if (r, c) == target and lin_steps >= 4:
                shortest = min(shortest, dists[key])

        print(shortest)

if __name__ == '__main__':
    main()
