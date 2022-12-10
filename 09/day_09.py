import math


def read_file():
    with open("input.txt") as file:
        return file.read().strip().split("\n")


def parse_motion(motion):
    direction, number = motion.split(" ")
    number = int(number)
    return direction, number


# How each move applies to coordinates
moves = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}


# Apply a move to coordinates
def make_move(origin, move):
    return tuple(map(sum, zip(origin, move)))


def find_move(ah, at):
    if ah > at:
        return 1
    elif ah < at:
        return -1
    else:
        return 0


def follow(leader, follower):
    if math.dist(leader, follower) >= 2:
        xh, yh = leader
        xt, yt = follower
        # If not on the same row and column, must make a diagonal move
        x = find_move(xh, xt)
        y = find_move(yh, yt)
        return make_move(follower, (x, y))
    else:
        return follower


def part_1():
    motions = read_file()
    head = (0, 0)
    tail = (0, 0)
    tail_positions = set()
    tail_positions.add(tail)
    for motion in motions:
        direction, number = parse_motion(motion)
        for _ in range(number):
            head = make_move(head, moves[direction])
            tail = follow(head, tail)
            tail_positions.add(tail)

    print(len(tail_positions))


def part_2():
    motions = read_file()
    head = (0, 0)
    tail = (0, 0)
    nodes = [(0, 0)] * 8
    tail_positions = set()
    tail_positions.add(tail)
    for motion in motions:
        direction, number = parse_motion(motion)
        for _ in range(number):
            head = make_move(head, moves[direction])

            for i, node in enumerate(nodes):
                nodes[i] = follow(head if i == 0 else nodes[i - 1], node)

            tail = follow(nodes[-1], tail)
            tail_positions.add(tail)

    print(len(tail_positions))


part_1()
part_2()
