import argparse


def solve1(pairs):
    ans = 0
    for pair in pairs:
        first, second = pair
        min_f, max_f = first
        min_s, max_s = second
        first_contained = min_f <= min_s and max_f >= max_s
        second_contained = min_s <= min_f and max_s >= max_f
        if first_contained or second_contained:
            ans += 1
    return ans


def solve2(pairs):
    ans = 0
    for pair in pairs:
        first, second = pair
        min_f, max_f = first
        min_s, max_s = second
        first_overlaps = max_f <= min_s
        second_overlaps = max_s <= min_f
        if first_overlaps or second_overlaps:
            ans += 1
    return ans


def parse_file(file):
    contents = file.read()
    ass_pairs = contents.split("\n")
    ass_pair_split = [pair.split(",") for pair in ass_pairs]
    return [
        tuple([tuple(int(n) for n in s.split("-")) for s in p]) for p in ass_pair_split
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=argparse.FileType(mode="r"), required=True)
    args = parser.parse_args()

    content = parse_file(args.file)
    args.file.close()
    print(solve1(content))
    print(solve2(content))


if __name__ == "__main__":
    main()
