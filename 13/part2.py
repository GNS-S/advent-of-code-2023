from part1 import parse_input

import numpy as np
import numpy.typing as npt

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grids = parse_input(f)

        total = 0
        for grid in grids:
            rows = row_almost_mirror_idx(grid)
            cols = row_almost_mirror_idx(grid.transpose())

            total += max(rows * 100, 0) + max(cols, 0)

        print(total)

def row_almost_mirror_idx(matrix: npt.NDArray) -> int:
    start, end = 1, len(matrix)
    for i in range(start, end):
        mirror_size = min(i, end - i)

        left = np.flip(matrix[i - mirror_size:i], axis=0)
        right = matrix[i:i + mirror_size]

        if np.invert(left == right).sum() == 1:
            return i

    return -1

if __name__ == '__main__':
    main()
