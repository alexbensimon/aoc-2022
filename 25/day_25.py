def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


SNAFU_VALUES = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}


def snafu_to_decimal(snafu: str):
    snafu_digits = list(snafu)
    snafu_digits.reverse()
    return sum(SNAFU_VALUES[digit] * (5**i) for i, digit in enumerate(snafu_digits))


def part_1():
    snafu_numbers = read_file()

    decimal_sum = sum(map(snafu_to_decimal, snafu_numbers))

    snafu_sum = []
    while decimal_sum:
        # Adding 2 allows to use the classic conversion where digits start at 0
        res, rem = divmod(decimal_sum + 2, 5)
        snafu_sum.append(list(SNAFU_VALUES.keys())[rem])
        decimal_sum = res
    snafu_sum.reverse()
    print("".join(snafu_sum))


part_1()
