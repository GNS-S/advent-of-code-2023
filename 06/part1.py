from math import prod

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        totals = []
        records = parse_input(f)

        for record in records:
            total_t, score = record
            beaten = 0

            for held_t in range(1, total_t + 1):
                if(s(total_t, held_t) > score):
                    beaten += 1

            totals.append(beaten)

        print(prod(totals))

def s(total_t: int, held_t: int):
    return held_t * (total_t - held_t)

def parse_input(file) -> list:
    lines = file.readlines()

    times = map(int, lines[0].split()[1:])
    scores = map(int, lines[1].split()[1:])

    return list(zip(times, scores))

if __name__ == '__main__':
    main()
