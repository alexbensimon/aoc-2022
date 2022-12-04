import re


def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def parse_line(line):
    regex = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    res = regex.search(line)
    return tuple(map(int, res.groups()))


def is_contained(sections):
    x1, x2, y1, y2 = sections
    return (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2)


def part_1():
    lines = read_file()
    assignments = map(parse_line, lines)
    contain = list(filter(is_contained, assignments))
    print(len(contain))


def is_overlap(sections):
    x1, x2, y1, y2 = sections
    return (
        (x1 >= y1 and x1 <= y2)
        or (x2 >= y1 and x2 <= y2)
        or (y1 >= x1 and y1 <= x2)
        or (y2 >= x1 and y2 <= x2)
    )


def part_2():
    lines = read_file()
    assignments = map(parse_line, lines)
    overlap = list(filter(is_overlap, assignments))
    print(len(overlap))


# part_1()
part_2()
