from typing import Optional

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        grid = parse_input(f)

        energized = count_energized(grid, (0, 0), (0, 1))
        print(energized)

def count_energized(grid: list[list[chr]], position: tuple[int, int], direction: tuple[int, int]) -> int:
    seen = beam(grid, position, direction)
    return len({ position for position, _ in seen })

def beam(
    grid: list[list[chr]],
    position: tuple[int, int],
    direction: tuple[int, int],
    seen: Optional[set]=None,
) -> Optional[int]:
    if seen is None:
        seen = set()

    max_r, max_c = len(grid), len(grid[0])
    r, c = position
    dr, dc = direction
    approach = (position, direction)

    while approach not in seen and 0 <= r < max_r and 0 <= c < max_c:
        seen.add(approach)
        tile = grid[r][c]

        if tile == '|' and dc != 0:
            beam(grid, (r - 1, c), (-1, 0), seen)
            beam(grid, (r + 1, c), ( 1, 0), seen)
        elif tile == '-' and dr != 0:
            beam(grid, (r, c - 1), (0, -1), seen)
            beam(grid, (r, c + 1), (0,  1), seen)
        else: 
            if tile == '/':
                dr, dc = -dc, -dr
            if tile == '\\':
                dr, dc = dc, dr

            r, c = r + dr, c + dc

        approach = ((r, c), (dr, dc))

    return seen

def parse_input(file) -> list[list[chr]]:
    grid = []
    for line in file:
        grid.append(list(line.strip()))

    return grid

if __name__ == '__main__':
    main()
