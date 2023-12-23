from part1 import parse_input, to_adjacency_matrix, dfs

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        maze = parse_input(f)
        start = (0, maze[0].index('.'))
        end = (len(maze) - 1, maze[-1].index('.'))
        
        no_slopes = []
        for row in maze:
            no_slopes.append(['.' if col in ['^', '>', 'v', '<'] else col for col in row])

        matrix = to_adjacency_matrix(no_slopes)

        print(dfs(matrix, start, end))

if __name__ == '__main__':
    main()
