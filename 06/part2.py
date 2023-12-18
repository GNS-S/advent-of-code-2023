from math import sqrt, floor, ceil

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        total = 0
        total_t, score = parse_input(f)

        xs = list(quadratic_inequality(1, -total_t, score))
        xs.sort()

        x1 = floor(xs[0])
        x2 = ceil(xs[1])

        print(x2 - x1 - 1)

def quadratic_inequality(a: int, b: int, c: int) -> tuple[int, int]:
    root_discriminant = sqrt(b**2 - 4 * a * c)

    x1 = (-b - root_discriminant)/(2 * a)
    x2 = (-b + root_discriminant)/(2 * a)

    return x1, x2

def parse_input(file) -> list:
    lines = file.readlines()

    time = int(''.join(lines[0].split()[1:]))
    score = int(''.join(lines[1].split()[1:]))

    return time, score

if __name__ == '__main__':
    main()
