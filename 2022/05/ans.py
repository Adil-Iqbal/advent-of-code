import re
import argparse


def solve1(content):
    stacks, instructions = content
    for moves in instructions:
        qty, src, dest = moves
        for _ in range(qty):
            stacks[dest].append(stacks[src].pop())

    ans = ""
    for stack in stacks:
        ans += stack.pop()
    return ans


def solve2(content):
    print("TODO! Make this work!")
    stacks, instructions = content
    for moves in instructions:
        qty, src, dest = moves
        for _ in range(qty):
            stacks[dest].append(stacks[src].pop())

    ans = ""
    for stack in stacks:
        ans += stack.pop()
    return ans


def parse_file(file):
    stacks = []
    instructions = []
    instruction_numeric_ptn = re.compile(r"move (\d+) from (\d+) to (\d+)")
    stackitem_ptn = re.compile(r"[A-Z]")
    stacklimit_ptn = re.compile(r"^[\s\d]+$")
    lines = file.read().split("\n")

    stacklimit_idx = 0
    for idx, line in enumerate(lines):
        if re.search(stacklimit_ptn, line):
            stacklimit_idx = idx

    num_stacks = int(lines[stacklimit_idx][-2])
    for _ in range(num_stacks):
        stacks.append([])

    for idx in reversed(range(stacklimit_idx)):
        line = lines[idx]
        stackcycle_idx = 0
        for i in range(0, len(line) - 1, 4):
            if m := re.search(stackitem_ptn, line[i : i + 4]):
                stacks[stackcycle_idx].append(m.group(0))
            stackcycle_idx += 1

    for i in range(stacklimit_idx + 2, len(lines)):
        m = re.match(instruction_numeric_ptn, lines[i])
        instructions.append((int(m[1]), int(m[2]) - 1, int(m[3]) - 1))

    return stacks, instructions


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
