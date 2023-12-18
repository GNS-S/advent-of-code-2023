from part1 import parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        games = parse_input(f)

        sortable_hands = []
        for (hand, bid) in games:
           hand_type, value = hand_value_j(hand)
           sortable_hands.append((hand_type, value, bid))

        sortable_hands.sort()

        total = sum([bid*(i + 1) for i, (_, _, bid) in enumerate(sortable_hands)])

        print(total)

def hand_value_j(hand: list[str]) -> int:
    hand_str = ''.join([sortable_char_j(card) for card in hand])

    return (hand_type_j(hand), hand_str)

def hand_type_j(hand: list[str]) -> int:
    js = hand.count('J')
    counts = {}

    for card in hand:
        if card != 'J':
            counts[card] = counts.get(card, 0) + 1

    totals = list(counts.values())
    totals.sort()

    if len(totals) > 0:
        totals[-1] = totals[-1] + js
    else:
        totals.append(js)
    
    if totals == [5]:
        return 7
    elif totals == [1, 4]:
        return 6
    elif totals == [2, 3]:
        return 5
    elif totals == [1, 1, 3]:
        return 4
    elif totals == [1, 2, 2]:
        return 3
    elif totals == [1, 1, 1, 2]:
        return 2
    else:
        return 1

def sortable_char_j(symbol: str) -> chr:
    if symbol.isdigit():
        return symbol
    elif symbol == 'J':
        return '1'
    else:
        return chr(ord('9') + ['T', 'Q', 'K', 'A'].index(symbol) + 1)

if __name__ == '__main__':
    main()
