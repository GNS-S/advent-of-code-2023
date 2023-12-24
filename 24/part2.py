from part1 import parse_input, intersect_xy

from math import ceil
import numpy as np
from numpy.typing import NDArray
from numpy.linalg import solve

# https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kepu26z
# 
# Given the thrown rock has position p_R and velocity v_R and the i-th hailstone
# p_i and v_i, we know that for every i at some time t_i that a collision occurs:
#
# p_R + t_i*v_R = p_i + t_i*v_i
#
# From here
# 1. p_R - p_i == t_i*(v_i - v_R)
# 2. (p_R - p_i) x (v_R - v_i) == t_i*(v_i - v_R) x (v_R - v_i) == 0
# Since the cross product of a vector with itself is 0:
#
# (p_R - p_i) x (v_R - v_i) == 0
# Then we can equate p_R and v_R to any two different pairs of indices to get a 6x6
# system of linear equations for p_R and v_R (since they are common to every i)

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        stones = parse_input(f)

        first_three = []
        for stone in stones[:3]:
            p, v = stone
            first_three.append({
                'p': np.array(p),
                'v': np.array(v)
            })

        h0, h1, h2 = first_three

        top_left = skew_symmetric_matrix(h0['v']) - skew_symmetric_matrix(h1['v'])
        bottom_left = skew_symmetric_matrix(h0['v']) - skew_symmetric_matrix(h2['v'])
        top_right = -skew_symmetric_matrix(h0['p']) + skew_symmetric_matrix(h1['p'])
        bottom_right = -skew_symmetric_matrix(h0['p']) + skew_symmetric_matrix(h2['p'])
        
        top = np.concatenate((top_left, top_right), axis=1)
        bottom = np.concatenate((bottom_left, bottom_right), axis=1)

        A = np.concatenate((top, bottom)) 
        B = np.concatenate([
            -np.cross(h0['p'], h0['v']) + np.cross(h1['p'], h1['v']),
            -np.cross(h0['p'], h0['v']) + np.cross(h2['p'], h2['v'])
        ])

        x, y, z, vx, vy, vz = solve(A, B)
        
        # Here pray to the floating point precision gods that ceiling this output will provide
        # the correct answer. A more rational approach would be rewriting all these calculations
        # using Python's own Decimal type. Feel free to do... that.
        print(ceil(sum([x, y, z])))

def skew_symmetric_matrix(vec3d: NDArray) -> NDArray:
    i, j, k = vec3d

    return np.array([
        [ 0, -k,  j],
        [ k,  0, -i],
        [-j,  i,  0]
    ])

if __name__ == '__main__':
    main()
