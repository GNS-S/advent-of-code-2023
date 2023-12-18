from part1 import parse_input

from math import prod
from collections import defaultdict

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        total = 0
        
        games = parse_input(f)

        for game_no, rounds in games:
            minimums = defaultdict(int)

            for rnd in rounds:
                for color in rnd:
                    if rnd[color] > minimums[color]:
                        minimums[color] = rnd[color]

            total += prod(minimums.values())

    print(total)

if __name__ == '__main__':
    main()
