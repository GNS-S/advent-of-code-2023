from part1 import parse_input, intersection

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        total = 0

        lines = parse_input(f)
        cards = []
        for winning, actual in lines:
            shared = intersection(winning, actual)
            cards.append(len(shared))

        total = sum([count_cards(cards, i) for i in range(len(cards))])
        print(total)

def count_cards(cards: list, index: int) -> int:
    won = cards[index]
    copy_sum = 0

    for i in range(index, index + won):
        copy_sum += count_cards(cards, i + 1)

    return 1 + copy_sum

if __name__ == '__main__':
    main()
