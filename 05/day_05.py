import re

# Quicker to copy this part of the input than parsing it
stacks_test = [
    "ZN",
    "MCD",
    "P",
]
stacks_input = [
    "RNFVLJSM",
    "PNDZFJWH",
    "WRCDG",
    "NBS",
    "MZWPCBFN",
    "PRMW",
    "RTNGLSW",
    "QTHFNBV",
    "LMHZNF",
]


def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def parse_line(line):
    regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
    res = regex.search(line)
    return tuple(map(int, res.groups()))


def part_1():
    stacks = list(map(list, stacks_input))
    lines = read_file()
    for line in lines:
        moves, origin, dest = parse_line(line)
        for _ in range(moves):
            # Take the last item of the origin stack and append it to the dest stack
            stacks[dest - 1].append(stacks[origin - 1].pop())
    res = "".join(map(lambda stack: stack[-1], stacks))
    print(res)


def part_2():
    stacks = list(map(list, stacks_input))
    lines = read_file()
    for line in lines:
        moves, origin, dest = parse_line(line)
        to_move = stacks[origin - 1][-moves:]
        stacks[origin - 1] = stacks[origin - 1][:-moves]
        stacks[dest - 1] = stacks[dest - 1] + to_move
    res = "".join(map(lambda stack: stack[-1], stacks))
    print(res)


part_1()
part_2()
