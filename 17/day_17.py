def get_patterns():
    with open("input.txt") as file:
        return list(file.read().strip())


shapes = [
    [["#", "#", "#", "#"]],
    [[".", "#", "."], ["#", "#", "#"], [".", "#", "."]],
    # Reversed so that coords from bottom right are correct
    [["#", "#", "#"], ["#", ".", "."], ["#", ".", "."]],
    [["#"], ["#"], ["#"], ["#"]],
    [["#", "#"], ["#", "#"]],
]

directions = {"<": (0, 1), ">": (0, -1), "v": (-1, 0)}

CAVE_WIDTH = 7


def shape_coords(shape):
    coords = []
    for r, row in enumerate(shape):
        for c, item in enumerate(row):
            coords.append(((r, c), item))

    return coords


def move_if_possible(shape, pos, n_pos, cave: dict):
    coords = shape_coords(shape)
    ap, bp = n_pos

    for coord, item in coords:
        if item == ".":
            continue

        ac, bc = coord
        an, bn = newc = (ap + ac, bp + bc)

        # check if not outside cave + no collision
        if an < 0 or bn < 0 or bn > CAVE_WIDTH - 1 or cave.get(newc) == "#":
            return pos, False

    return n_pos, True


def new_pos(pos, direction):
    return (pos[0] + direction[0], pos[1] + direction[1])


def stop_shape(shape, pos, cave: dict):
    coords = shape_coords(shape)
    ap, bp = pos

    for coord, item in coords:

        ac, bc = coord
        newc = (ap + ac, bp + bc)

        if cave.get(newc) != "#":
            cave[newc] = item

    return cave


def compute_shape_starting_position(shape, cave: dict):
    a_highest_rock = (
        max(coords[0] for coords, item in cave.items() if item == "#") if cave else -1
    )
    a_shape = a_highest_rock + 4

    shape_width = len(shape[0])
    b_shape = CAVE_WIDTH - 2 - shape_width

    return (a_shape, b_shape)


def print_cave(cave: dict):
    height = max(coords[0] for coords, item in cave.items() if item == "#")

    for a in range(height, -1, -1):
        for b in range(CAVE_WIDTH - 1, -1, -1):
            print(cave[(a, b)] if cave.get((a, b)) else ".", end="")
        print("")


def play_shape(shape, pos, patterns, cave):
    while True:
        if not patterns:
            patterns = get_patterns()

        # First pattern (right or left)
        pattern = patterns.pop(0)
        pos, _ = move_if_possible(shape, pos, new_pos(pos, directions[pattern]), cave)

        # Then, down
        pos, has_moved = move_if_possible(
            shape, pos, new_pos(pos, directions["v"]), cave
        )

        if not has_moved:
            cave = stop_shape(shape, pos, cave)
            break

    return patterns, cave


def part_1():
    patterns = []
    cave = {}

    for i in range(2022):
        shape = shapes[i % 5]
        # starting position is bottom right of shape
        pos = compute_shape_starting_position(shape, cave)

        patterns, cave = play_shape(shape, pos, patterns, cave)

    # print_cave(cave)
    print(max(coords[0] for coords, _ in cave.items()) + 1)


def find_cycle(height_changes: list):
    MIN_CYCLE_SIZE = 20
    start = 0
    size = MIN_CYCLE_SIZE

    while start < len(height_changes):
        end = start + size
        if end + size > len(height_changes):
            start += 1
            size = MIN_CYCLE_SIZE
            continue
        if height_changes[start:end] == height_changes[end : end + size]:
            return start, size
        size += 1


def part_2():
    patterns = []
    cave = {}
    previous_height = 0
    changes = []

    for i in range(5000):
        shape = shapes[i % 5]
        # starting position is bottom right of shape
        pos = compute_shape_starting_position(shape, cave)

        patterns, cave = play_shape(shape, pos, patterns, cave)

        new_height = max(coords[0] for coords, _ in cave.items()) + 1
        height_change = new_height - previous_height
        previous_height = new_height
        # Register height change after each rock is placed
        changes.append(height_change)

    total_rocks = 1000000000000
    # Find the pattern
    start, size = find_cycle(changes)
    cycle_height = sum(changes[start : start + size])
    cycles = (total_rocks - start) // size
    rem = (total_rocks - start) % size
    outside_cycle_height = sum(changes[0 : start + rem])

    res = outside_cycle_height + cycles * cycle_height
    print(res)


part_1()
part_2()
