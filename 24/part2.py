from part1 import parse_input

from itertools import combinations
from math import floor
import numpy as np

# Given x, y, z, vx, vy, vz is the position and velocity of the throw
#       hxi, hyi, hyz, hvxi, hvyi, hvzi is the position and  velocity of the i-th hailstone
#
# By subtracting the throws initial position and velocity from a hailstone we can create a system
# where each hailstone passes through the origin point - meaning its new position is a multiple of its
# new velocity. Representing this dependency for 2 dimensions looks like this:
#
# (hxi - x) / (hyi - y) = (hvxi - vx) / (hdyi - vy)
#
# By choosing 4 pairs of hailstones, filling in the values and subtracting the equations for each pair
# we can populate a 4 row matrix to compute x, y, vx, vy - and repeat for y, z, vy, vz

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        stones = parse_input(f)

        four_pairs = list(combinations(stones, 2))[:4]

        Axy = []
        Ayz = []
        bxy = []
        byz = []
        for pair in four_pairs:
            h1, h2 = pair
            h1p, h1v = h1
            h2p, h2v = h2

            xs, rhs = matrix_row(*h1p[:2], *h1v[:2], *h2p[:2], *h2v[:2])
            Axy.append(xs)
            bxy.append(rhs)

            xs, rhs = matrix_row(*h1p[1:], *h1v[1:], *h2p[1:], *h2v[1:])
            Ayz.append(xs)
            byz.append(rhs)

        x, y, vx, vy = np.linalg.solve(Axy, bxy)
        y, z, vy, vz = np.linalg.solve(Ayz, byz)

        # Here we mutter a little prayer to the floating point gods that this will be precise enough 
        print(floor(sum([x, y, z])))

def matrix_row(hx1: int, hy1: int, hvx1: int, hvy1: int, hx2: int, hy2: int, hvx2: int, hvy2: int) -> list[int]:
    x  =  hvy2 - hvy1
    y  = -hvx2 + hvx1
    vx = -hy2 + hy1 
    vy =  hx2 - hx1

    rhs = hvx1 * hy1 - hvx2 * hy2 + hx2 * hvy2 - hx1 * hvy1

    return [x, y, vx, vy], rhs

if __name__ == '__main__':
    main()
