from part1 import parse_input

def main():
    INPUT_PATH = './input.txt'

    with open(INPUT_PATH) as f:
        results = []
        seeds, fns = parse_input(f)

        seed_ranges = pair_seed_ranges(seeds)

        for r in seed_ranges:
            start, offset = r
            end = start + offset
            ranges = [(start, end)]

            for fn in fns:
                ranges = apply_to_ranges(fn, ranges)
            
            results.append(min(ranges)[0])

        closest = min(results)
        print(closest)

def apply_to_ranges(fns: list[tuple[int, int, int]], ranges: list[tuple[int, int]]) -> int:
    applied = []
    ranges_left = ranges

    for (fn_s, fn_e, offset) in fns:
        out_of_range = []

        while ranges_left:
            r_s, r_e = ranges_left.pop()

            overlap = (max(fn_s, r_s), min(fn_e, r_e))
            if (overlap[1] > overlap[0]):
                applied.append((overlap[0] + offset, overlap[1]+offset))

            before = (r_s, min(fn_s, r_e))
            if (before[1] > before[0]):
                out_of_range.append(before)

            after = (max(fn_e, r_s), r_e)
            if (after[1] > after[0]):
                out_of_range.append(after)

        ranges_left = out_of_range

    return applied + ranges_left

def pair_seed_ranges(seeds: list[int]) -> list[list[int]]:
    return list(zip(seeds[::2], seeds[1::2]))

if __name__ == '__main__':
    main()
