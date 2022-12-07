def read_file():
    with open("input.txt") as file:
        return file.read().strip()


def is_marker(chars):
    # A set removes the duplicates
    return len(chars) == len(set(chars))


def find_marker(size):
    chars = list(read_file())
    index = size
    while index < len(chars):
        size_chars = chars[index - size : index]
        if is_marker(size_chars):
            print(index)
            break
        index += 1


def part_1():
    find_marker(4)


def part_2():
    find_marker(14)


# part_1()
# part_2()
