def read_file():
    with open("input.txt") as file:
        grid, path = file.read().split("\n\n")

        grid = grid.split("\n")
        max_len = len(max(grid, key=len))
        # Pad grid lines
        grid = [list(line.ljust(max_len)) for line in grid]

        path = list(path.strip())
        instructions = []
        num = ""
        while path:
            char = path.pop(0)
            if char.isnumeric():
                num += char
            else:
                instructions.append(int(num))
                instructions.append(char)
                num = ""
        if num:
            instructions.append(int(num))

        return grid, instructions


facings = [">", "v", "<", "^"]


def turn(facing, direction):
    match (direction):
        case "R":
            new_i = (facings.index(facing) + 1) % len(facings)
        case "L":
            new_i = facings.index(facing) - 1

    return facings[new_i]


def find_tile_position(grid, r_start, r_end, c_start, c_end):
    for r in range(r_start, r_end, -1 if r_start > r_end else 1):
        for c in range(c_start, c_end, -1 if c_start > c_end else 1):
            if grid[r][c] != " ":
                return r, c


def move(grid, facing, position):
    # Get next position
    r, c = position
    match facing:
        case ">":
            next_position = (
                (r, c + 1)
                if c + 1 < len(grid[r]) and grid[r][c + 1] != " "
                else find_tile_position(grid, r, r + 1, 0, c)
            )
        case "v":
            next_position = (
                (r + 1, c)
                if r + 1 < len(grid) and grid[r + 1][c] != " "
                else find_tile_position(grid, 0, r, c, c + 1)
            )
        case "<":
            next_position = (
                (r, c - 1)
                if c > 0 and grid[r][c - 1] != " "
                else find_tile_position(grid, r, r + 1, len(grid[r]) - 1, c)
            )
        case "^":
            next_position = (
                (r - 1, c)
                if r > 0 and grid[r - 1][c] != " "
                else find_tile_position(grid, len(grid) - 1, r, c, c + 1)
            )
    rn, cn = next_position
    # If can move, return next position
    if grid[rn][cn] == ".":
        return next_position
    # Else return current position
    return position


def part_1():
    grid, instructions = read_file()

    facing = ">"
    position = find_tile_position(grid, 0, 1, 0, len(grid[0]))

    while instructions:
        instruction = instructions.pop(0)

        if type(instruction) is str:
            facing = turn(facing, instruction)
            continue

        for _ in range(instruction):
            position = move(grid, facing, position)

    r, c = position
    print(1000 * (r + 1) + 4 * (c + 1) + facings.index(facing))


def move_cube(grid, facing, position):
    # Get next position
    next_facing = facing
    r, c = position
    match facing:
        case ">":
            if c + 1 < len(grid[r]) and grid[r][c + 1] != " ":
                next_position = (r, c + 1)
            else:
                if r < 50:
                    next_position = (149 - r, 99)
                    next_facing = "<"
                elif 50 <= r < 100:
                    next_position = (49, 50 + r)
                    next_facing = "^"
                elif 100 <= r < 150:
                    next_position = (149 - r, 149)
                    next_facing = "<"
                elif 150 <= r < 200:
                    next_position = (149, r - 100)
                    next_facing = "^"
        case "v":
            if r + 1 < len(grid) and grid[r + 1][c] != " ":
                next_position = (r + 1, c)
            else:
                if c < 50:
                    next_position = (0, c + 100)
                    next_facing = "v"
                elif 50 <= c < 100:
                    next_position = (100 + c, 49)
                    next_facing = "<"
                elif 100 <= c < 150:
                    next_position = (c - 50, 99)
                    next_facing = "<"
        case "<":
            if c > 0 and grid[r][c - 1] != " ":
                next_position = (r, c - 1)
            else:
                if r < 50:
                    next_position = (149 - r, 0)
                    next_facing = ">"
                elif 50 <= r < 100:
                    next_position = (100, r - 50)
                    next_facing = "v"
                elif 100 <= r < 150:
                    next_position = (149 - r, 50)
                    next_facing = ">"
                elif 150 <= r < 200:
                    next_position = (0, r - 100)
                    next_facing = "v"
        case "^":
            if r > 0 and grid[r - 1][c] != " ":
                next_position = (r - 1, c)
            else:
                if c < 50:
                    next_position = (c + 50, 50)
                    next_facing = ">"
                elif 50 <= c < 100:
                    next_position = (100 + c, 0)
                    next_facing = ">"
                elif 100 <= c < 150:
                    next_position = (199, c - 100)
                    next_facing = "^"
    rn, cn = next_position
    # If can move, return next position
    if grid[rn][cn] == ".":
        return next_position, next_facing
    # Else return current position
    return position, facing


def part_2():
    grid, instructions = read_file()

    facing = ">"
    position = find_tile_position(grid, 0, 1, 0, len(grid[0]))

    while instructions:
        instruction = instructions.pop(0)

        if type(instruction) is str:
            facing = turn(facing, instruction)
            continue

        for _ in range(instruction):
            position, facing = move_cube(grid, facing, position)

    r, c = position
    print(1000 * (r + 1) + 4 * (c + 1) + facings.index(facing))


part_1()
part_2()
