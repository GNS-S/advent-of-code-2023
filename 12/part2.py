from part1 import combinations, parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        rows = parse_input(f)
        
        total = 0
        for (springs, broken) in rows:
            springs5 = 4 * (springs + ['?']) + springs
            broken5 = 5 * broken

            total += combinations(springs5, broken5, 0, {})

        print(total)

if __name__ == '__main__':
    main()
