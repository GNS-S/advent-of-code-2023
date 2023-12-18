def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        total = 0
        
        for line in f:
            digits = get_digits(line.strip())
            total += int(digits[0] + digits[-1])

    print(total)

def get_digits(string: str) -> list[str]:
    word_forms = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = []
    for index, char in enumerate(string):
        if char.isdigit():
            digits.append(char)
        for word_index, word in enumerate(word_forms):
            if (string[index:].startswith(word)):
                digits.append(str(word_index + 1))
            
    return digits

if __name__ == '__main__':
    main()
