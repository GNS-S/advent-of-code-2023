from part1 import parse_input

from math import prod

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        flows, _ = parse_input(f)

        possible_ops = ['<', '>']
        ranges = { c: (1, 4000) for c in 'xmas' }
        
        Q = [('in', ranges)]
        
        total = 0
        while Q:
            state, ranges = Q.pop()

            if state == 'R':
                continue
            if state == 'A':
                # Operating on inclusive ranges! e.g. [1, 3] spans 3 elements
                total += prod([h - l + 1 for (l, h) in ranges.values()])
                continue

            flow = flows[state]
            for step in flow.split(','):
                if ':' not in step:
                    Q.append((step, ranges))
                else:
                    rule, on_pass = step.split(':')
                    op = next(op for op in possible_ops if op in rule)
                    attr, value = rule.split(op)

                    keep, push = split_ranges(ranges, attr, op, int(value))

                    if push:
                        Q.append((on_pass, push))
                    if keep is None:
                        break
                    ranges = keep
                        
        print(total)

def split_ranges(ranges: dict, attr: str, op: str, value: int, START=1, END=4000) -> tuple:
    # delta start, delta end, reverse return order
    transforms_by_op = {
        '<': (-1, 0, True),
        '>': ( 0, 1, False)
    }
    ds, de, reverse = transforms_by_op[op]
    op_ranges = [(START, value + ds), (value + de, END)]

    if reverse:
        op_ranges.reverse()
    
    return tuple(intersect(ranges, attr, r) for r in op_ranges)

def intersect(ranges: dict, attr: str, op_range: tuple) -> dict | None:
    l1, h1 = ranges[attr]
    l2, h2 = op_range
    l, h = (max(l1, l2), min(h1, h2))

    if l > h:
        return None
    else:
        return { **ranges, attr: (l, h) }

if __name__ == '__main__':
    main()
