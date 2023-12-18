from part1 import parse_input
import numpy as np

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        total = 0

        seqs = parse_input(f)
        for seq in seqs:
            total += solve(seq)

        print(total)

def solve(seq: list[int]) -> int:
    diffs = np.diff(seq)
    if all(diffs == 0):
        return seq[0]
    else:
        return seq[0] - solve(diffs)

if __name__ == '__main__':
    main()
