def build_grid():
    with open("input.txt") as file:
        lines = file.read().strip().split("\n")
        grid = {}
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "#":
                    grid[(r, c)] = char
        return grid


def has_neighbor(position, grid: dict):
    r, c = position
    for i in range(-1, 2):
        for j in range(-1, 2):
            p = (r + i, c + j)
            if grid.get(p) and p != position:
                return True
    return False


def do_round(grid, directions):
    proposed = {}

    # Propose moves
    for elf in grid.keys():
        if not has_neighbor(elf, grid):
            continue

        r, c = elf
        for direction in directions:
            if not any(grid.get((r + i, c + j)) for i, j in direction):
                i, j = direction[0]
                proposed.setdefault((r + i, c + j), []).append(elf)
                break

    # End if no proposed move
    if not proposed:
        return True, grid, directions

    # Execute moves
    for p, elves in proposed.items():
        if len(elves) == 1:
            elf = elves[0]
            del grid[elf]
            grid[p] = "#"

    # Change directions priority
    directions.append(directions.pop(0))

    return False, grid, directions


def initial_directions():
    return [
        # North
        ((-1, 0), (-1, -1), (-1, 1)),
        # South
        ((1, 0), (1, -1), (1, 1)),
        # West
        ((0, -1), (1, -1), (-1, -1)),
        # East
        ((0, 1), (1, 1), (-1, 1)),
    ]


def part_1():
    grid = build_grid()
    directions = initial_directions()

    # 10 rounds
    for _ in range(10):
        _, grid, directions = do_round(grid, directions)

    r_list = [r for r, _ in grid.keys()]
    c_list = [c for _, c in grid.keys()]
    height = abs(min(r_list) - max(r_list)) + 1
    width = abs(min(c_list) - max(c_list)) + 1

    empty_count = height * width - len(grid.keys())
    print(empty_count)


def part_2():
    grid = build_grid()
    directions = initial_directions()

    round = 0
    while True:
        round += 1
        end, grid, directions = do_round(grid, directions)
        if end:
            break

    print(round)


part_1()
part_2()
