from math import inf
from pprint import pprint
import enum
import argparse


def to_priority(ch):
    c = ord(ch)
    if 65 <= c <= 90:
        return c - (65 - 27)
    return c - (97 - 1)


def solve2(rucksacks):
    ans = 0
    for i in range(0, len(rucksacks), 3):
        r1, r2, r3 = rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]
        r1_set = set(r1)
        r2_set = set(r2)
        for c in r3:
            if c in r1_set and c in r2_set:
                ans += (pr := to_priority(c))
                break
    return ans


def solve1(rucksacks):
    ans = 0
    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        comp1, comp2 = rucksack[0:mid], rucksack[mid:]
        comp_set = set(comp1)
        for c in comp2:
            if c in comp_set:
                ans += (pr := to_priority(c))
                break
    return ans


def parse_file(file):
    contents = file.read()
    return contents.split("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=argparse.FileType(mode="r"), required=True)
    args = parser.parse_args()
    content = parse_file(args.file)
    print(solve1(content))
    print(solve2(content))
    args.file.close()


if __name__ == "__main__":
    main()
