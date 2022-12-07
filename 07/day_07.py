import pprint
import re
from functools import reduce


def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def build_fs():
    lines = read_file()
    wd = []  # working directory
    fs = {}  # file system

    re_cd_back = re.compile(r"\$ cd \.\.")
    re_cd = re.compile(r"\$ cd (.+)")
    re_ls = re.compile(r"\$ ls")
    re_dir = re.compile(r"dir (\w+)")
    re_file = re.compile(r"(\d+) .+")

    for line in lines:
        if re_cd_back.search(line):
            wd.pop()

        elif re_cd.search(line):
            dir = re_cd.search(line).group(1)
            wd.append(dir)

        elif re_ls.search(line):
            continue

        elif re_dir.search(line):
            dir = re_dir.search(line).group(1)
            # We represent a path as "/.a.e"
            fs.setdefault(".".join(wd), []).append(".".join(wd) + "." + dir)

        elif re_file.search(line):
            size = re_file.search(line).group(1)
            fs.setdefault(".".join(wd), []).append(size)

    return fs


# We could cache this function to avoid computing the same sizes multiple times
def compute_size(fs, dir):
    return reduce(
        # If the value is int, it's a file size, else it's a directory and we recursively compute its size
        lambda acc, val: acc + (int(val) if val.isnumeric() else compute_size(fs, val)),
        fs[dir],
        0,
    )


def part_1():
    fs = build_fs()
    # pprint.pprint(fs)

    sizes = map(lambda key: compute_size(fs, key), fs.keys())
    res = sum(filter(lambda size: size <= 100000, sizes))
    print(res)


def part_2():
    fs = build_fs()
    sizes = list(map(lambda key: compute_size(fs, key), fs.keys()))

    total_space = 70000000
    used_space = sizes[0]  # The first one is the root
    unused_space = total_space - used_space
    needed_space = 30000000
    missing_space = needed_space - unused_space

    sizes.sort()
    # Get the first directory with enough space
    size = next(size for size in sizes if size > missing_space)

    print(size)


part_1()
part_2()
