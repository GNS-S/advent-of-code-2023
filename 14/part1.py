def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)
        n_grid = roll_north(grid)
        
        size = len(n_grid)
        total = 0

        for i, row in enumerate(n_grid):
            total += row.count('O') * (size - i)

        print(total)

def roll_north(grid: list[list[chr]]) -> list[list[chr]]:
    new = [[''] * len(row) for row in grid]

    rows = range(len(new))
    cols = range(len(new[0]))

    for r in rows:
        for c in cols:
            e = grid[r][c]
            
            if e != 'O':
                new[r][c] = e
            else:
                prev = r - 1
                while prev >= 0 and new[prev][c] == '.':
                    prev -= 1

                new[r][c] = '.'
                new[prev + 1][c] = 'O'

    return new

def parse_input(file) -> list[list[chr]]:
    rows = []
    for line in file:
        rows.append(list(line.strip()))

    return rows

if __name__ == '__main__':
    main()
