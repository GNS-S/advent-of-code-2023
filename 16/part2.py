from part1 import parse_input, count_energized

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)
        rows, cols = len(grid), len(grid[0])
        
        highest = 0
        for r in range(rows):
            highest = max(highest, count_energized(grid, (r, 0), (0, 1)))
            highest = max(highest, count_energized(grid, (r, len(grid[r]) - 1), (0, -1)))

        for c in range(cols):
            highest = max(highest, count_energized(grid, (0, c), (1, 0)))
            highest = max(highest, count_energized(grid, (len(grid) - 1, c), (-1, 0)))

        print(highest)

if __name__ == '__main__':
    main()
