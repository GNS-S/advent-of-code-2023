def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        steps, nodes = parse_input(f)

        current = 'AAA'
        i = 0
        while current != 'ZZZ':
            step = steps[i % len(steps)]
            idx = step_to_idx(step)
            current = nodes[current][idx]
            i += 1

        print(i)

def step_to_idx(step: str) -> int:
    return ['L', 'R'].index(step)

def parse_input(file) -> list:
    steps, mapping = file.read().strip().split('\n\n')

    nodes = {}
    steps = list(steps.strip())

    for line in mapping.split('\n'):
        node, branches = line.split('=')
        node = node.strip()
        branches = branches.strip()
        branches = branches[1:len(branches) - 1].split(', ')

        nodes[node] = branches

    return steps, nodes

if __name__ == '__main__':
    main()
