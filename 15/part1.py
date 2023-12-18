def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        steps = parse_input(f)

        total = 0
        for step in steps:
            total += ascii_hash(step)
        
        print(total)

def ascii_hash(string: str) -> int:
    current = 0
    for c in string:
       current += ord(c) 
       current *= 17 
       current %= 256

    return current

def parse_input(file) -> list[str]:
    steps = file.read().strip().split(',')

    return steps

if __name__ == '__main__':
    main()
