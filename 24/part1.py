from itertools import combinations
from math import inf, isclose

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        stones = parse_input(f)

        in_test_area = lambda x: 200000000000000 <= x <= 400000000000000

        total = 0
        for a, b in combinations(stones, 2):
            (ax, ay, az), (vax, vay, vaz) = a
            axy = (ax, ay), (vax, vay)

            (bx, by, bz), (vbx, vby, vbz) = b
            bxy = (bx, by), (vbx, vby)

            intersect = intersect_xy(axy, bxy)
            if intersect:
                (x, y), is_future = intersect

                is_within_bounds = in_test_area(x) and in_test_area(y)

                if is_future and is_within_bounds:
                    total += 1

        print(total)

def intersect_xy(a: tuple, b: tuple) -> None | tuple:
    (ax, ay), (vax, vay) = a
    a_slope = inf if vax == 0 else vay / vax
    a_intercept = ay - a_slope * ax

    (bx, by), (vbx, vby) = b
    b_slope = inf if vbx == 0 else vby / vbx
    b_intercept = by - b_slope * bx

    if isclose(a_slope, b_slope):
        return None

    x = (b_intercept - a_intercept) / (a_slope - b_slope)
    y = x * a_slope + a_intercept

    is_future_a = (x > ax) == (vax > 0)
    is_future_b = (x > bx) == (vbx > 0)
    is_future = is_future_a and is_future_b

    return (x, y), is_future

def parse_input(file) -> list[list[chr]]:
    stones = []

    for line in file:
        coords, movement = line.strip().split(' @ ')
        xyz = [int(c) for c in coords.split(', ')]
        velocity = [int(m) for m in movement.split(', ')]
        stones.append((xyz, velocity))

    return stones

if __name__ == '__main__':
    main()
