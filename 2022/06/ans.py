import copy
import argparse


def solve1(content, n=4):
    for i, _ in enumerate(content):
        if i < n - 1:
            continue
        if len(set((substr := content[i : i + n]))) == n:
            return i + n


def solve2(content):
    return solve1(content, n=14)


def parse_file1(content):
    return content


def parse_file2(content):
    return parse_file1(content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=argparse.FileType(mode="r"), required=True)
    args = parser.parse_args()

    content1 = args.file.read()
    content2 = copy.deepcopy(content1)
    args.file.close()
    print(solve1(parse_file1(content1)))
    print(solve2(parse_file2(content2)))


if __name__ == "__main__":
    main()
