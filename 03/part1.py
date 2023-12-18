from re import finditer

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        total = 0

        lines = f.readlines()
        
        for index, line in enumerate(lines):
            for match in finditer(r'[0-9]+', line.strip()):
                s, e = max(match.start() - 1, 0), min(match.end() + 1, len(line) - 1)

                side = any(map(is_symbol, line[s:e]))
                top = any(map(is_symbol, lines[index - 1][s:e])) if index - 1 >= 0 else False
                bottom = any(map(is_symbol, lines[index + 1][s:e])) if index + 1 < len(lines) else False

                if any([side, top, bottom]):
                    total += int(match.group())

        print(total)

def is_symbol(x: str) -> bool:
    return not x.isdigit() and x != '.'
        
if __name__ == '__main__':
    main()
