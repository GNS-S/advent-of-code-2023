def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        total = 0

        lines = parse_input(f)
        for winning, actual in lines:
            shared = intersection(winning, actual)
            if len(shared) != 0:
                total += 2**(len(shared) - 1)

        print(total)

def parse_input(file) -> list[tuple[list, list]]:
    lines = []

    for line in file:
        game_id, numbers = line.strip().split(': ')
        winning, actual = numbers.split(' | ')
        lines.append((winning.split(), actual.split()))
    
    return lines

def intersection(a: list, b: list) -> list:
    return list(set(a) & set(b))

if __name__ == '__main__':
    main()
