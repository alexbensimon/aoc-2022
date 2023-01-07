import math


def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def part_1():
    instructions = read_file()
    i = 0
    to_add = 0
    X = 1
    strength = 0
    for cycle in range(1, 221):
        if cycle % 40 == 20:
            strength += cycle * X

        if to_add != 0:
            X += to_add
            to_add = 0
            i += 1
        else:
            instruction = instructions[i]
            if instruction == "noop":
                i += 1
            elif instruction.startswith("addx"):
                to_add = int(instruction.split(" ")[1])

    print(strength)


def part_2():
    instructions = read_file()
    i = 0
    to_add = 0
    X = 1
    pixels = [""] * 6
    for cycle in range(1, 241):
        row = math.floor((cycle - 1) / 40)
        col = (cycle - 1) % 40
        pixel = "#" if col in range(X - 1, X + 2) else "."
        pixels[row] = pixels[row] + pixel

        if to_add != 0:
            X += to_add
            to_add = 0
            i += 1
        else:
            instruction = instructions[i]
            if instruction == "noop":
                i += 1
            elif instruction.startswith("addx"):
                to_add = int(instruction.split(" ")[1])

    print("\n".join(pixels))


part_1()
part_2()
