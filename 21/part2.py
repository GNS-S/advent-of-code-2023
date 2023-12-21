from part1 import parse_input, count_stops

from collections import deque

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid, start = parse_input(f)

        assert len(grid) == len(grid[0])
        size = len(grid)

        # https://en.wikipedia.org/wiki/Newton_polynomial#Newton_forward_divided_difference_formula
        goal = 26501365
        n = goal // size
        remainder = goal % size

        y0 = count_stops(grid, start, remainder, loop_grid=True)
        y1 = count_stops(grid, start, remainder + size, loop_grid=True)
        y2 = count_stops(grid, start, remainder + size * 2, loop_grid=True)

        d0 = y0
        d1 = y1 - y0
        d2 = (y2 - y1) - (y1 - y0)

        f = lambda x: d0 + d1 * x + d2 * (x * (x - 1)) // 2

        print(f(n))

if __name__ == '__main__':
    main()
