# Heavily inspired by (and by inspired I mean down right ripped off of - it's very clean)
# https://www.reddit.com/r/adventofcode/comments/18qbsxs/comment/ketzp94
from random import choice

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        vertices, edges = parse_input(f)
        subset1, subset2 = karger(vertices, edges)
        print(len(subset1) * len(subset2))

# https://en.wikipedia.org/wiki/Karger%27s_algorithm
def karger(vertices: set, edges: set) -> list[set]:
    minimum_cuts = -1

    while minimum_cuts != 3:
        subsets = [{v} for v in vertices]
        vertice_subset = lambda v: next(s for s in subsets if v in s)
        
        while len(subsets) > 2:
            u, v = choice([*edges])
            s1, s2 = vertice_subset(u), vertice_subset(v)
            if s1 != s2:
                s1 |= s2; 
                subsets.remove(s2)
        
        minimum_cuts = sum(vertice_subset(u) != vertice_subset(v) for u, v in edges)

    return subsets

def parse_input(file) -> tuple[set, set]:
    vertices = set()
    edges = set()

    for line in file:
        vertice, rest = line.strip().split(': ')
        adjacents = rest.split()

        vertices |= { vertice, *adjacents }
        edges |= { (vertice, adj) for adj in adjacents }

    return vertices, edges

if __name__ == '__main__':
    main()
