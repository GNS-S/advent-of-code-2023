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
        return seq[-1]
    else:
        return seq[-1] + solve(diffs)

def parse_input(file) -> list[list[int]]:
    sequences = []
    for line in file:
        sequences.append([int(x) for x in line.strip().split()])

    return sequences

if __name__ == '__main__':
    main()
