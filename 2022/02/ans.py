from math import inf
from pprint import pprint
import enum
import argparse

R = 1
P = 2
S = 3
W = 6
D = 3
L = 0


def solve2(strarr):
    trans = {"A": R, "B": P, "C": S, "X": L, "Y": D, "Z": W}
    out_dict = {
        (R, W): P,
        (R, D): R,
        (R, L): S,
        (P, W): S,
        (P, D): P,
        (P, L): R,
        (S, W): R,
        (S, D): S,
        (S, L): P,
    }
    score = 0
    for s in strarr:
        if len(s) == 3:
            ops, outs = s.split(" ")
            op, out = trans[ops], trans[outs]
            resp = out_dict[op, out]
            score += resp + out
    return score


def solve1(strarr):
    trans = {"A": R, "B": P, "C": S, "X": R, "Y": P, "Z": S}

    out_dict = {
        (R, R): D,
        (P, P): D,
        (S, S): D,
        (R, S): W,
        (P, R): W,
        (S, P): W,
        (R, P): L,
        (P, S): L,
        (S, R): L,
    }
    score = 0
    for s in strarr:
        if len(s) == 3:
            os, rs = s.split(" ")
            op, r = trans[os], trans[rs]
            out = out_dict[r, op]
            score += r + out
    return score


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
