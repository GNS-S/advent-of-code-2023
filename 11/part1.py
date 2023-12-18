import numpy as np
import numpy.typing as npt

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        initial = parse_input(f)
        chart = expand(initial)

        indices = np.argwhere(chart == '#')
        coords = [tuple(idx) for idx in indices]

        total = 0
        for i, (ax, ay) in enumerate(coords):
            for (bx, by) in coords[i + 1:]:
                total += abs(ax - bx) + abs(ay - by)

        print(total)

def expand(chart: npt.NDArray) -> npt.NDArray:
    expanded = chart.copy()

    for axis in [0, 1]:
        offset = 0
        for i in range(chart.shape[axis]):
            values = np.take(chart, i, axis)
            if all(values == '.'):
                expanded = np.insert(expanded, i + offset, '.', axis)
                offset += 1

    return expanded

def parse_input(file) -> npt.NDArray:
    rows = []
    for line in file:
        cols = np.array(list(line.strip()))
        rows.append(cols)

    return np.array(rows)

if __name__ == '__main__':
    main()
