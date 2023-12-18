def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        results = []
        seeds, fns = parse_input(f)

        for seed in seeds:
            x = seed
            for fn in fns:
                x = one_from_range_fns(fn, x)

            results.append(x)

        closest = min(results)
        print(closest)


def one_from_range_fns(fns: list[tuple[int, int, int]], x: int) -> int:
    for fn in fns:
        start, end, offset = fn
        if start <= x < end:
            return x + offset
    return x 

def parse_input(file) -> tuple[list, dict]:
    splits = file.read().strip().split('\n\n')

    seeds = list(map(int, splits[0].split(': ')[1].split()))

    range_fns = []

    for split in splits[1:]:
        fn_group = []
        mapping_lines = split.split('\n')
                
        for mapping in mapping_lines[1:]:
            dest_start, src_start, span = list(map(int, mapping.split()))
            start, end, offset = src_start, src_start + span, dest_start - src_start
            fn_group.append((start, end, offset))

        range_fns.append(fn_group)
            
    return seeds, range_fns

if __name__ == '__main__':
    main()
