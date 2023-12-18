def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        plan = parse_input(f)

        vertices, boundary = to_cartesian(plan)
        area = shoelace(vertices)
        interior = picks_interior(area, boundary)

        print(interior + boundary)

# https://en.wikipedia.org/wiki/Pick's_theorem
def picks_interior(area: int, boundary: int) -> int:
    return int(area - boundary / 2 + 1)

# https://en.wikipedia.org/wiki/Shoelace_formula
def shoelace(points: list[tuple]) -> int:
    total = 0
    for i in range(len(points) - 1):
        xi, yi = points[i]
        xj, yj = points[i + 1]

        total += xi * yj - xj * yi

    return int(abs(total) / 2)

def to_cartesian(plan: tuple[tuple, int]) -> tuple[list[tuple], int]:
    current = (0, 0)
    vertices = list([current])
    boundary = 0

    for p in plan:
        (dr, dc), steps = p
        r, c = current
        new = r + dr * steps, c + dc * steps

        boundary += steps
        vertices.append(new)
        current = new
         
    return vertices, boundary

def parse_input(file) -> tuple[tuple, int]:
    directions = {
        'U': ( 1,  0),
        'R': ( 0,  1),
        'D': (-1,  0),
        'L': ( 0, -1),
    }

    plan = []
    for line in file:
        direction, steps, _ = line.strip().split()
        direction = directions[direction]
        steps = int(steps)

        plan.append((direction, steps))

    return plan

if __name__ == '__main__':
    main()
