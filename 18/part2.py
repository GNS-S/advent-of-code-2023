from part1 import picks_interior, shoelace, to_cartesian

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        plan = parse_input(f)

        vertices, boundary = to_cartesian(plan)
        area = shoelace(vertices)
        interior = picks_interior(area, boundary)

        print(interior + boundary)

def parse_input(file) -> tuple[tuple, int]:
    directions = [( 0,  1), (-1,  0), ( 0, -1), ( 1,  0)]

    plan = []
    for line in file:
        _, _, hexsplit = line.strip().split()
        hexcode = hexsplit[2:len(hexsplit) - 1]

        direction = directions[int(hexcode[-1])]
        steps = int(hexcode[:-1], 16)
    
        plan.append((direction, steps))

    return plan

if __name__ == '__main__':
    main()
