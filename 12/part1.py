def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        rows = parse_input(f)
        
        total = 0
        for (springs, broken) in rows:
            total += combinations(springs, broken, 0, {})

        print(total)

def combinations(array: list[chr], groups: list[int], hashes: int, memo: dict) -> int:
    state = (str(array), str(groups), hashes)
    if state in memo:
        return memo[state]

    if len(array) == 0:
        if (len(groups) == 1 and hashes == groups[0]) or (len(groups) == 0 and hashes == 0):
            return 1
        else:
            return 0

    total = 0
    
    for c in ['#', '.']:
        if array[0] == '?' or array[0] == c:
            if c == '#':
                total += combinations(array[1:], groups, hashes + 1, memo)

            if c == '.':
                if hashes == 0:
                    total += combinations(array[1:], groups, 0, memo)

                if hashes > 0 and len(groups) != 0 and groups[0] == hashes:
                    total += combinations(array[1:], groups[1:], 0, memo)

    memo[state] = total
    return total

def parse_input(file) -> list[tuple]:
    rows = []
    for line in file:
        springs_str, broken_str = line.strip().split()
        springs = list(springs_str)
        broken = [int(b) for b in broken_str.split(',')]
        rows.append((springs, broken))
        
    return rows

if __name__ == '__main__':
    main()
