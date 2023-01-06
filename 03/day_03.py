def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def get_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def part_1():
    lines = read_file()
    common_items = [
        "".join(set(line[: (len(line) // 2)]).intersection(line[(len(line) // 2) :]))
        for line in lines
    ]
    sum_priorities = sum(map(get_priority, common_items))
    print(sum_priorities)


def part_2():
    lines = read_file()
    buckets = list(zip(*[iter(lines)] * 3))
    common_items = [
        "".join(set(bucket[0]) & set(bucket[1]) & set(bucket[2])) for bucket in buckets
    ]
    sum_priorities = sum(map(get_priority, common_items))
    print(sum_priorities)


part_1()
part_2()
