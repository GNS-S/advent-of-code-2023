from part1 import parse_input, lower_bricks

from collections import deque

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        bricks = parse_input(f)
        structure = lower_bricks(bricks)
            
        total = 0
        for brick in structure:
            total += collapsing_chain_len(structure, brick) - 1

        print(total)

def collapsing_chain_len(structure: dict, start: str) -> int:
    collapsed = set({ start })
    Q = deque([start])
    
    while Q:
        brick = Q.popleft()
        supports = structure[brick]['supports']

        for dependant in supports:
            if all(beam in collapsed for beam in structure[dependant]['supported_by']):
                collapsed.add(dependant)
                Q.append(dependant)
    
    return len(collapsed)

if __name__ == '__main__':
    main()
