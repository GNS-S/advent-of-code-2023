def main():
    INPUT_PATH = './input.txt'
    MAXIMUMS = { 'red': 12, 'green': 13, 'blue': 14 }

    with open(INPUT_PATH) as f:
        total = 0

        games = parse_input(f)
        
        for game_no, rounds in games:
            valid_game = True
            for rnd in rounds:
                for color in rnd:
                    if rnd[color] > MAXIMUMS[color]:
                        valid_game = False
                        
            if valid_game:
                total += game_no

    print(total)

def parse_input(file) -> tuple[int, dict[str, int]]:
    games = []

    for line in file:
        game, data = line.split(':')
        game_no = int(game.split(' ')[1])

        rounds = []
        for rnd in data.strip().split(';'):
            parsed = {}
            by_color = rnd.strip().split(', ')

            for result in by_color:
                number, color = result.split(' ')
                parsed[color] = int(number)
                    
            rounds.append(parsed)

        games.append((game_no, rounds))

    return games

if __name__ == '__main__':
    main()
