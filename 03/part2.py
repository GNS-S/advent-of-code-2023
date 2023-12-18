from re import finditer
from math import prod

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        total = 0

        lines = f.readlines()

        line_numbers = []        
        for index, line in enumerate(lines):
            numbers = []
            for match in finditer(r'[0-9]+', line.strip()):
                numbers.append(match)

            line_numbers.append(numbers)

        for index, line in enumerate(lines):
            numbers = []
            for match in finditer(r'\*', line.strip()):
                s, e = max(match.start() - 1, 0), min(match.end() + 1, len(line) - 1)

                is_overlapping = lambda nmbr: max(nmbr.start(), s) < min(nmbr.end(), e)

                side = filter(is_overlapping, line_numbers[index])
                top = filter(is_overlapping, line_numbers[index - 1]) if index - 1 >= 0 else []
                bottom = filter(is_overlapping, line_numbers[index + 1]) if index + 1 < len(line_numbers) else []

                matches = list([int(match.group()) for match in [*side, *top, *bottom]])
                if len(matches) == 2:
                    total += prod(matches)

        print(total)

if __name__ == '__main__':
    main()
