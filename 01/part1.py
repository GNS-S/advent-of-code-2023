def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        total = 0
        
        for line in f:
            digits = get_digits(line.strip())
            total += int(digits[0] + digits[-1])

    print(total)

def get_digits(string: str) -> list[str]:
    digits = []
    for char in string:
        if char.isdigit():
            digits.append(char)
            
    return digits

if __name__ == '__main__':
    main()
