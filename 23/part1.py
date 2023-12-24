def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        maze = parse_input(f)
        start = (0, maze[0].index('.'))
        end = (len(maze) - 1, maze[-1].index('.'))

        matrix = to_adjacency_matrix(maze)
        print(dfs(matrix, start, end))

def dfs(matrix: dict, start: tuple, end: tuple) -> int:
    distances = []
    Q = [(start, 0, set())]

    while Q:
        current, distance, visited = Q.pop()

        if current == end:
            distances.append(distance)
            continue

        visited = visited.copy()
        visited.add(current)
        
        for vert in matrix[current]:
            if vert not in visited:
                cost = matrix[current][vert]
                Q.append((vert, distance + cost, visited))
    
    return max(distances)

def to_adjacency_matrix(maze: list):
    max_r, max_c = len(maze), len(maze[0])
    
    matrix = {}

    for r in range(max_r):
        for c in range(max_c):
            position = (r, c)
            if maze[r][c] != '#':
                matrix[position] = {}
                adjacents = get_adjacent(maze, position)
                for adj in adjacents:
                    matrix[position][adj] = 1

    verts = list(matrix.keys())
    for vert in verts:
        adjacents = matrix[vert]
        if len(adjacents) == 2:
            left, right = adjacents.keys()
            if vert in matrix[left] and vert in matrix[right]:
                longest = max(matrix[left].get(right, 0),  adjacents[left] + adjacents[right])
                
                del matrix[left][vert]
                del matrix[right][vert]
                del matrix[vert]

                matrix[left][right] = longest
                matrix[right][left] = longest

    return matrix

def get_adjacent(maze: list, position: tuple) -> list[tuple]:
    r, c = position
    max_r, max_c = len(maze), len(maze[0])
    deltas = [(1,  0), (0, 1), (-1, 0), (0, -1)]
    direction_by_tile = {
        '.': [0, 1, 2, 3],
        '^': [2],
        '>': [1],
        'v': [0],
        '<': [3]
    }

    adjacents = []
    for direction in direction_by_tile[maze[r][c]]:
        dr, dc = deltas[direction]
        new_r = r + dr
        new_c = c + dc
        in_maze = 0 <= new_r < max_r and 0 <= new_c < max_c

        if in_maze and maze[new_r][new_c] != '#':
            adjacents.append((new_r, new_c))

    return adjacents

def parse_input(file) -> list[list[chr]]:
    rows = []

    for line in file:
        rows.append(list(line.strip()))

    return rows

if __name__ == '__main__':
    main()
