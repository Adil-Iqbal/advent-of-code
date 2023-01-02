from math import inf
from pprint import pprint
import argparse


def solve(file):
    contents = file.read()
    strarr = contents.split("\n")
    intarr = []
    for s in strarr:
        if s:
            intarr.append(int(s))
        else:
            intarr.append(-1)

    all_ts = []
    t = 0
    for n in intarr:
        if n != -1:
            t += n
        else:
            all_ts.append(t)
            t = 0
    all_ts.sort(reverse=True)
    return sum(all_ts[:3])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=argparse.FileType(mode="r"), default=None)
    args = parser.parse_args()
    print(solve(args.file))
    args.file.close()


if __name__ == "__main__":
    main()
