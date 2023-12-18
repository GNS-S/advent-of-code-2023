from part1 import parse_input, step_to_idx
from math import lcm

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        steps, nodes = parse_input(f)

        current = [node for node in nodes if node[-1] == 'A']
        loops_at = {}
        i = 0

        while len(loops_at) != len(current):
            step = steps[i % len(steps)]
            idx = step_to_idx(step)
            current = [nodes[node][idx] for node in current]
            for j, node in enumerate(current):
                if node[-1] == 'Z' and j not in loops_at:
                    loops_at[j] = i + 1
            i += 1

        distances = loops_at.values()

        print(lcm(*distances))

if __name__ == '__main__':
    main()
