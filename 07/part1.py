def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        games = parse_input(f)

        sortable_hands = []
        for (hand, bid) in games:
           hand_type, value = hand_value(hand)
           sortable_hands.append((hand_type, value, bid))

        sortable_hands.sort()

        total = sum([bid*(i + 1) for i, (_, _, bid) in enumerate(sortable_hands)])

        print(total)

def hand_value(hand: list[str]) -> int:
    hand_str = ''.join([sortable_char(card) for card in hand])

    return (hand_type(hand), hand_str)

def hand_type(hand: list[str]) -> int:
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1

    totals = list(counts.values())
    totals.sort()
    
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

def sortable_char(symbol: str) -> chr:
    if symbol.isdigit():
        return symbol
    else:
        return chr(ord('9') + ['T', 'J', 'Q', 'K', 'A'].index(symbol) + 1)

def parse_input(file) -> list:
    games = []

    for line in file:
        cards_str, bid_str = line.strip().split()
        
        cards = list(cards_str)
        bid = int(bid_str)

        games.append((cards, bid))

    return games

if __name__ == '__main__':
    main()
