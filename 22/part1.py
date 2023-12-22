def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        bricks = parse_input(f)
        structure = lower_bricks(bricks)
            
        total = 0
        for brick in structure:
            dependants = structure[brick]['supports']
            if all([len(structure[beam]['supported_by']) > 1 for beam in dependants]):
                total += 1

        print(total)

def lower_bricks(bricks: list[tuple]) -> tuple[list, dict, dict]:
    lowest_first = sorted(bricks, key=lambda x: x[0][-1])
    lowered = []
    structure = {}

    for brick in lowest_first:
        (x1, y1, z1), (x2, y2, z2), brick_no = brick
        structure[brick_no] = {
            'supports': [],
            'supported_by': []
        }
        delta = 1 - z1

        for below in reversed(lowered):
            (_, _, _), (_, _, bz2), _ = below
            lowers_by = bz2 - z1 + 1
            if lowers_by > delta and xy_intersects(brick, below):
                delta = lowers_by
        
        lowered_brick = (x1, y1, z1 + delta), (x2, y2, z2 + delta), brick_no

        directly_under = [l for l in lowered if l[1][2] == lowered_brick[0][2] - 1]
        supports_brick = [l[2] for l in directly_under if xy_intersects(lowered_brick, l)]

        for support in supports_brick:
            structure[brick_no]['supported_by'].append(support)
            structure[support]['supports'].append(brick_no)

        lowered.append(lowered_brick)

    return structure

def xy_intersects(a: tuple, b: tuple) -> bool:
    (ax1, ay1, _), (ax2, ay2, _), _ = a
    (bx1, by1, _), (bx2, by2, _), _ = b

    x_intersects = range_intersects((ax1, ax2), (bx1, bx2))
    y_intersects = range_intersects((ay1, ay2), (by1, by2))

    return x_intersects and y_intersects

def range_intersects(a: tuple, b: tuple) -> bool:
    a1, a2 = a
    b1, b2 = b
    return max(a1, b1) <= min(a2, b2)

def parse_input(file) -> list[tuple]:
    bricks = []

    for i, line in enumerate(file):
        start, end = line.strip().split('~')
        st_xyz= [int(c) for c in start.split(',')]
        ed_xyz = [int(c) for c in end.split(',')]

        bricks.append((tuple(st_xyz), tuple(ed_xyz), i))

    return bricks

if __name__ == '__main__':
    main()
