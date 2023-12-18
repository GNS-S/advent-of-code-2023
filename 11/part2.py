from part1 import parse_input

import numpy as np
import numpy.typing as npt

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:        
        chart = parse_input(f)

        expansion_times = 1000000
        expanded = get_expanded_indices(chart)

        indices = np.argwhere(chart == '#')
        coords = [tuple(idx) for idx in indices]

        total = 0
        for i, (ax, ay) in enumerate(coords):
            for (bx, by) in coords[i + 1:]:
                x1, x2 = sorted([ax, bx])
                y1, y2 = sorted([ay, by])

                crossed_xs = len([x for x in expanded['xs'] if x1 <= x <= x2])
                crossed_ys = len([y for y in expanded['ys'] if y1 <= y <= y2])
                crossed = crossed_xs + crossed_ys

                total += (x2 - x1) + (y2 - y1) + crossed * (expansion_times - 1)

        print(total)

def get_expanded_indices(chart: npt.NDArray) -> npt.NDArray:
    expanded = ([], [])
    for axis in [0, 1]:
        offset = 0
        for i in range(chart.shape[axis]):
            values = np.take(chart, i, axis)
            if all(values == '.'):
                expanded[axis].append(i)

    rows, cols = expanded
    return { 'xs': rows, 'ys': cols }

if __name__ == '__main__':
    main()
