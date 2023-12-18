from part1 import parse_input, roll_north

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)
        
        memo = {}
        cycles = 1000000000
        i = 0
        while i != cycles:
            key = hash_grid(grid)
            next_i = i + 1

            if (key in memo):
                grid, last_i = memo[key]
                diff = i - last_i
                skippable_loops = int((cycles - i) // diff)

                if skippable_loops != 0:
                    next_i = min(cycles, skippable_loops * diff + i + 1)

            memo[key] = (grid, i)
            grid = tilt_cycle(grid)
            i = next_i

        size = len(grid)
        total = 0
        for i, row in enumerate(grid):
            total += row.count('O') * (size - i)

        print(total)

def tilt_cycle(grid: list[list[chr]]) -> list[list[chr]]:
    result = grid

    for _ in range(4):
        result = rotate_clockwise(roll_north(result)) 

    return result

def rotate_clockwise(grid: list[list[chr]]) -> list[list[chr]]:
    return [list(tpl) for tpl in zip(*grid[::-1])]

def hash_grid(grid: list[list[chr]]) -> int:
    # Even simple string compression (e.g. {number}{character}) would work well here too
    return hash(''.join([''.join(r) for r in grid]))

if __name__ == '__main__':
    main()
