from part1 import parse_input, ascii_hash

from collections import defaultdict

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        steps = parse_input(f)
        
        focals = defaultdict(int)
        boxes = defaultdict(list)
        for step in steps:
            if '-' in step:
                to_remove = step.replace('-', '')
                box = ascii_hash(to_remove)

                if to_remove in boxes[box]:
                    boxes[box].remove(to_remove)
            elif '=' in step:
                label, focal = step.split('=')
                focals[label] = int(focal)
                box = ascii_hash(label)

                if label not in boxes[box]:
                    boxes[box].append(label)

        total = 0
        for box in boxes:
            for i, label in enumerate(boxes[box]):
                total += (box + 1) * (i + 1) * focals[label]

        print(total)

if __name__ == '__main__':
    main()
